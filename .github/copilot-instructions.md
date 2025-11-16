# IACA Project - AI Agent Instructions

## What is IACA?

**IACA** (Infrastructure as Code Architect) is a system design and documentation framework that extends Infrastructure-as-Code concepts to support **arbitrary resource types** using an Entity-Component-System (ECS) architecture. Unlike traditional IaC tools, IACA handles incomplete/abstract components, human tasks, planning elements, and requirements—making it useful for designing entire systems end-to-end, not just for deployment automation.

## Core Architecture

### Entity-Component-System (ECS) Model

The project uses ECS where:
- **Entities**: Uniquely identified by `entity` keys (e.g., a patient, a workflow, a requirement)
- **Components**: Uniquely identified by `(entity, comp_key)` pairs. Typed data attached to entities, stored as DataFrames (one per component type)
- **Registry**: Central `data.Registry` object managing all component DataFrames with special components:
  - `compinst`: Master index tracking all component instances across entity/comp_key pairs
  - `compdef`: Component definitions specifying schemas, multiplicities, validation rules

### Key Data Structures

**Field Definition Syntax** (from YAML manifests):
```yaml
field_name [dtype|multiplicity] = default_value: description
```
Example: `patient_id [str|1..1]`: A required string field with exactly one value per entity.

**Component Multiplicity**:
- `0..1` or `1..1`: Indexed by `entity` only
- `0..*` or `1..*`: Multi-indexed by `(entity, comp_key)`

## ETL Pipeline

The main workflow is **Extract → Load → Transform** via `Architect.perform_registry_etl()`:

1. **Extract**: Parse YAML manifests (`extract_yaml.py`) and Python docstrings (`extract_python.py`)
2. **Load**: Build `Registry` with `compinst` tracking
3. **Preprocess Transforms**:
   - `ComponentNormalizer`: Standardize component schemas
   - `ComponentDefExtractor`: Extract `compdef` from `component` + `fields` 
   - `ComponentValidator`: Validate against schemas using Pandera
4. **System Transforms**:
   - `LinksParser`: Parse link syntax into graph edges
   - `LinkCollector`: Aggregate links from components with `link_type` tags
   - `GraphAnalyzer`: Build NetworkX MultiDiGraph from links
   - `RequirementAnalyzer`: Analyze requirement hierarchies and coverage
5. **Postprocess**: Final validation

## Development Workflows

### Running Tests
```bash
# Run all tests from project root using uv
uv run pytest

# Run specific test file
uv run pytest tests/test_etl.py

# Tests use unittest.TestCase, not pytest fixtures
```

There are two types of tests:
- standalone Python tests in `tests/`, intended for development and debugging
- registry-embedded tests declared using components and defined in `iaca/system_tests.py`. These tests validate the user's registry data and logic when `Architect.validate_registry()` is called.

**Key test patterns**:
- Tests are defined as functions/classes in Python files (`tests/test_*.py`)
- `Architect.validate_registry()` dynamically discovers and runs tests from the registry with priority filtering

### Working with Manifests

**Base manifest location**: `base_manifest/*.yaml` - defines core system components (required for all projects)

**User manifests**: Specified via `Architect(filename_patterns=['./path/*.yaml'])`

**Viewing entities**:
```python
registry.view_entity('entity_name', output_yaml=True, print_output=True)
```

**Key component types in base manifest**:
- `component`, `fields`: Define component schemas
- `requirement`, `satisfies`, `status`: Track requirements and implementation state
- `task`, `links`: Define workflows and dependencies
- `test`, `code`: Embed validation logic

### Common Operations

**Creating/updating components**:
```python
registry.set('component_name', dataframe, mode='upsert')  # Merge with existing
registry['component_name'] = dataframe  # Overwrite mode shortcut
```

**Querying components**:
```python
registry['component_name']  # Get single component DataFrame
registry.view(['comp_a', 'comp_b'], join_how='left')  # Join multiple components
```

**Parameter management**:
```python
registry.set_parameter_entity('default_parameters')
value = registry.get_parameter_set('param_name')
```

## Project-Specific Conventions

### Code Style

**Docstrings**: Use **NumPy-style docstrings** for all Python code. Include Parameters, Returns, and other sections as appropriate.

**Verbosity**: Prefer concise, direct implementations. Avoid unnecessary verbosity in:
- Code comments (only when adding clarity)
- Variable names (descriptive but brief)
- Function implementations (favor clarity over exhaustive documentation)
- Explanations (get to the point)

### Docstring Metadata
Python docstrings can contain YAML-formatted metadata blocks parsed as components:
```python
"""
Description text here.

Metadata
--------
- status: in production
- satisfies: requirement_name
- todo:
    value: Fix this later
    priority: 0.7
"""
```

### Link Syntax
Links between entities use pipe-delimited syntax in YAML:
```yaml
links: |
    entity_a --> entity_b
    entity_b --> entity_c
```

### Transformer Pattern
All transforms inherit from `BaseEstimator, TransformerMixin` (scikit-learn style):
- Implement `transform(dataframe, registry)` returning modified DataFrame
- Applied via `TransformSystem.apply_transform()`

## Common Pitfalls

1. **Index confusion**: Components have either `entity` index OR `(entity, comp_key)` multi-index depending on multiplicity
2. **Registry mutation**: Most registry methods return copies; use `.set()` or `[]` assignment to persist changes

## Key Files to Reference

- `iaca/data.py`: `Registry`, `Field`, `View` classes
- `iaca/etl.py`: `ExtractSystem`, `TransformSystem`, full ETL pipeline
- `iaca/sketch.py`: `Architect` class - main entry point
- `base_manifest/*.yaml`: System component definitions (component, requirement, task, etc.)
- `tests/test_data/healthcare_example/`: Real-world example project

## Dependencies & Environment

- **Package Manager**: This project uses **`uv`** for Python package management. Always use `uv` commands instead of `pip` or plain `python`:
  - Run tests: `uv run pytest` (not `python -m pytest` or `pytest`)
  - Run Python scripts: `uv run python script.py`
  - Install packages: `uv add package-name`
  - Sync dependencies: `uv sync`
- Python 3.13+ required
- Core: pandas, pandera, networkx, pyyaml
- Testing: pytest (but tests use unittest.TestCase)
- Notebooks: jupyterlab for exploration
- No React usage despite package.json (likely legacy/planned frontend)
