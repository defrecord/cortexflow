# Development Workflow

This document outlines the development workflow for the CortexFlow project.

## Mise en Place (Setting Up)

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/defrecord/cortexflow.git
cd cortexflow

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"
```

### Workspace Organization

The repository is organized as follows:

- `src/` - Source code organized by component
- `.duplicate/` - Git submodules of original repositories for reference
- `docs/` - Documentation files
- `tests/` - Test suite
- `examples/` - Example applications

## Development Workflow

### Feature Migration Process

1. **Reference Original Implementation**
   - Locate the feature in the appropriate submodule in `.duplicate/`
   - Understand its design, dependencies, and integration points

2. **Design Migration Plan**
   - Determine how the feature fits into the CortexFlow architecture
   - Identify necessary modifications or improvements
   - Document design decisions

3. **Implementation**
   - Create the necessary module structure
   - Implement the feature following CortexFlow coding standards
   - Add appropriate documentation

4. **Testing**
   - Add unit tests for the new feature
   - Add integration tests for interactions with other components
   - Verify functionality matches or improves upon the original

5. **Documentation**
   - Update relevant documentation files
   - Add examples demonstrating the feature
   - Mark the feature as completed in FEATURE_MIGRATION.md

### Branch Strategy

- `main` - Stable integration branch
- `feature/component-name/feature-name` - Feature branches
- `bugfix/issue-number` - Bug fix branches

### Code Review Process

All changes should go through code review:

1. Create a pull request with clear description
2. Ensure all tests pass
3. Address feedback from reviewers
4. Squash commits before merging

## Testing Guidelines

- Unit tests should be written for all new code
- Integration tests should verify component interactions
- Run full test suite before creating pull requests
- Test coverage should remain at or above 80%

## Documentation Guidelines

- All public APIs must be documented
- Use docstrings for function and class documentation
- Keep README and high-level docs up to date
- Add examples for new features

## Mise en Place Commands

```bash
# Run tests
pytest

# Check code style
flake8 src tests
black --check src tests
isort --check src tests

# Generate documentation
cd docs && make html

# Run example application
python examples/simple_agent_hierarchy.py
```