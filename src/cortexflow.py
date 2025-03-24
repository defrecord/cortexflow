"""CortexFlow - Integrated cognitive agent system.

This module provides the main entry point for the CortexFlow system.
"""

from typing import Dict, Optional, Any

from .agents.hierarchy import AgentHierarchy
from .memory.persistence import MemoryStore
from .cognitive.workflow import CognitiveWorkflow
from .shell.interface import ShellInterface
from .core.intelligence import Intelligence


class CortexFlow:
    """Main entry point for the CortexFlow system.
    
    This class integrates all the components of the system and provides
    a unified interface for working with intelligent agents.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the CortexFlow system.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        
        # Initialize components
        self.hierarchy = AgentHierarchy(self.config.get("hierarchy"))
        self.memory = MemoryStore(self.config.get("memory"))
        self.cognitive = CognitiveWorkflow(self.config.get("cognitive"))
        self.shell = ShellInterface(self.config.get("shell"))
        self.intelligence = Intelligence(self.config.get("intelligence"))
        
        # Set up default shell commands
        self._setup_shell_commands()
    
    def _setup_shell_commands(self) -> None:
        """Set up default shell commands."""
        self.shell.register_command(
            "agents", 
            lambda args: f"Agents: {list(self.hierarchy.agents.keys())}",
            "List all registered agents"
        )
        
        self.shell.register_command(
            "memory", 
            lambda args: f"Memory keys: {list(self.memory.memories.keys())}",
            "List all memory keys"
        )
        
        self.shell.register_command(
            "exit", 
            lambda args: "Exiting...",
            "Exit the shell"
        )
    
    def start_shell(self) -> None:
        """Start the interactive shell."""
        print("CortexFlow Shell")
        print("Type 'help' for a list of commands")
        
        while True:
            try:
                command = input("> ")
                if command.lower() == "exit":
                    break
                    
                result = self.shell.execute_command(command)
                print(result)
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")
    
    def create_agent(self, agent_id: str, agent_type: str, 
                    config: Optional[Dict[str, Any]] = None,
                    parent_id: Optional[str] = None) -> Any:
        """Create a new agent and add it to the hierarchy.
        
        Args:
            agent_id: Unique identifier for the agent
            agent_type: Type of agent to create
            config: Optional agent configuration
            parent_id: Optional parent agent ID
            
        Returns:
            The created agent
        """
        # TODO: Implement actual agent creation
        agent = {"type": agent_type, "config": config or {}}
        self.hierarchy.add_agent(agent_id, agent, parent_id)
        return agent