"""Interactive shell interface.

Integrates functionality from mindflow-shell to provide a command-line
interface for direct agent interaction.
"""

from typing import Dict, List, Optional, Any, Callable
import time


class ShellInterface:
    """Command-line interface for interacting with agents.
    
    This class provides a text-based interface for users to interact with
    the agent system directly.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the shell interface.
        
        Args:
            config: Optional configuration dictionary
        """
        self.commands = {}
        self.history = []
        self.config = config or {}
    
    def register_command(self, name: str, handler: Callable[[List[str]], str], 
                        help_text: str) -> None:
        """Register a new command.
        
        Args:
            name: Command name
            handler: Function that handles the command
            help_text: Help text for the command
        """
        self.commands[name] = {
            "handler": handler,
            "help": help_text
        }
    
    def execute_command(self, command_line: str) -> str:
        """Execute a command.
        
        Args:
            command_line: Full command line to execute
            
        Returns:
            Command output
        """
        parts = command_line.strip().split()
        if not parts:
            return ""
            
        command = parts[0].lower()
        args = parts[1:]
        
        self.history.append({
            "command": command_line,
            "timestamp": time.time()
        })
        
        if command == "help":
            return self._help_command(args)
        
        if command in self.commands:
            try:
                return self.commands[command]["handler"](args)
            except Exception as e:
                return f"Error: {str(e)}"
        
        return f"Unknown command: {command}"
    
    def _help_command(self, args: List[str]) -> str:
        """Handle the help command.
        
        Args:
            args: Command arguments
            
        Returns:
            Help text
        """
        if not args:
            commands = sorted(self.commands.keys())
            return "Available commands: " + ", ".join(commands)
        
        command = args[0].lower()
        if command in self.commands:
            return f"{command}: {self.commands[command]['help']}"
        
        return f"Unknown command: {command}"