# Contributing 

Thank you for your interest in contributing to the Awesome Ontologies collection. This document outlines the process for submitting ontologies to the dump folder and improving the repository.

## Adding Ontologies to the Dump Folder

### File Structure

All ontologies should be placed directly in the `assets/dump` folder:```
assets/
├── dump/
│   ├── [ontology-name].[ext]
│   ├── [another-ontology].[ext]
│   └── ...
```

Where:
- `[ontology-name].[ext]` is the ontology file (.owl, .ttl, .rdf, etc.)
- Use descriptive names to avoid conflicts

Naming Conventions
KEEP ORIGINAL NAME (so to help avoid duplicates)

## Important: README Update Required

**All contributions must include updates to the main README.md file.** Your ontology should be added to the appropriate section (Upper-Level, Mid-Level, Domain Ontologies, etc.) following the existing format:

```markdown
- [Ontology Name](link-to-source) - Brief description of the ontology.
```

Contributions that don't include README updates will not be accepted.

## Contribution Process

### Manual
1. Navigate to the repository on GitHub on `assets/dump`
2. Click the "Add file" button and select "Create new file"
3. In the file name field, enter the path: `assets/dump/[your-ontology-name].[ext]`
4. Upload your ontology file by either:
   - Dragging and dropping the file into the editor
   - Clicking "uploading an existing file" and selecting your file
5. Add a commit message describing your addition
6. Click "Commit new file"
7. **Edit the README.md file** to add your ontology to the appropriate section
8. Click "Pull request" to create a PR
9. Fill in the PR description with:
   - Ontology name and version
   - Brief description
   - Source URL
   - License information
10. Submit the pull request


### Code 
1. **Fork** the repository
2. **Create a branch** for your addition (`git checkout -b add-ontology-name`)
3. **Add the ontology** to the `assets/dump` folder
4. **Update the main README.md** to include your ontology in the appropriate section
5. **Submit a Pull Request** with a clear description of the added ontology

## Pull Request Guidelines

When submitting a PR, please:

1. Ensure your ontology file is properly formatted
2. Verify that the README.md has been updated with your ontology
3. Include information about the ontology in your PR description:
   - Name and version: 
   - Brief description: 
   - Source URL:
   - License information:

## Review Criteria

Submissions will further evaluated based on:

- **Quality**: Is the ontology well-designed and maintained?
- **Relevance**: Does it fit the scope of this collection?
- **License**: Is it available under an open license?
- **Accessibility**: Can others easily use it?

## Code of Conduct

- Be respectful and inclusive in all communications
- Give credit to original authors and maintainers
- Provide constructive feedback
- Help others improve their contributions

Thank you for helping build a valuable resource for the ontology community! 
