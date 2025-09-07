# Zero to Three: Project Organization

This document defines the organizational structure for the "Zero to Three" book project to maintain consistency and clarity as the project grows.

## Current Structure

```
zero_to_three/
├── README.md                           # Project overview and navigation
├── book/                              # Main book content
│   ├── SUMMARY.md                     # Book table of contents
│   ├── company-index.md              # Comprehensive case study compendium
│   ├── 00-preface.md                 # Front matter files
│   ├── 02-introduction.md            # Introduction
│   ├── 97-epilogue.md                # Back matter files
│   ├── 98-appendix.md
│   ├── part-1-the-new-paradigm/
│   ├── part-2-learning-from-failure/
│   ├── part-3-technical-and-organizational-innovations/
│   ├── part-4-crypto-native-models/
│   ├── part-5-three-leading-systems/
│   └── part-6-the-new-geography-of-innovation/
├── resources/                         # Supporting materials
│   ├── project-organization.md       # This file - organizational guidelines  
│   ├── images/                       # Diagrams, charts, photos
│   ├── templates/                    # Chapter templates, case study formats
│   └── research/                     # Background research, interview notes
└── drafts/                           # Work-in-progress content
    ├── outlines/                     # Chapter outlines and planning
    ├── fragments/                    # Partial content and ideas
    └── archive/                      # Old versions and discarded content
```

## File Naming Conventions

### Chapters
- **Format**: `chXX-descriptive-name.md` where XX is the chapter number (zero-padded)
- **Examples**: `ch01-the-new-paradigm.md`, `ch18-alternative-funding.md`, `ch32-global-coordination.md`
- **Title Format**: Include chapter number and title as H1 header within the file
- **Location**: Within appropriate `part-#-description/` directories
- **⚠️ CRITICAL**: Each chapter number must be unique across the entire book. No duplicate chapter numbers allowed.

### Case Studies
- **Main File**: `company-index.md` (comprehensive case study compendium)
- **Individual Studies**: If needed, use format `case_study_[company_name].md`
- **Examples**: `case_study_anthropic.md`, `case_study_tsmc.md`
- **Integration**: Case studies are embedded within relevant chapters rather than standalone files

### Supporting Documents
- **Outlines**: `outline_chapter_XX.md` or `outline_[topic].md`
- **Research**: `research_[topic].md` or `interview_[person_date].md`
- **Templates**: `template_[purpose].md`

## Version Management and Duplicate Prevention

### No Duplicate Chapters Policy
**ABSOLUTE RULE**: Each chapter number can only exist once in the entire book project.

- ✅ **Correct**: `ch18-alternative-funding.md` (one file with this number)
- ❌ **NEVER**: `ch18-alternative-funding.md` AND `ch18-building-what-works.md`
- ❌ **NEVER**: Multiple versions of same chapter number in different directories

### Chapter Conflicts Resolution
When chapter conflicts arise:

1. **Immediate Action**: Identify which chapter should retain the number
2. **Renumber**: Assign conflicting chapter to available sequential number
3. **Update References**: Fix all internal links and table of contents
4. **Document Change**: Note renumbering in commit message

### Alternative Versions Management

If you need to create alternative versions of the book:

#### Option 1: Versions Directory Structure
```
zero_to_three/
├── book/                    # Main canonical version
├── versions/
│   ├── v1-original/
│   │   └── book/           # Complete alternative version
│   ├── v2-expanded/
│   │   └── book/           # Another complete version
│   └── experimental/
│       └── book/           # Experimental version
├── resources/
└── drafts/
```

#### Option 2: Git Branch Strategy (Preferred)
```bash
git checkout -b version/alternative-structure
# Create your alternative version
git checkout main  # Return to canonical version
```

#### Option 3: Fork Repository
- Fork the entire repository for substantial rewrites
- Clearly mark as derivative work
- Maintain attribution to original

### Version Identification Requirements
Any alternative version MUST include:

1. **Clear Naming**: Version directory/branch name indicates it's not canonical
2. **Documentation**: README explaining differences from main version  
3. **Attribution**: Clear credit to original work and contributors
4. **Date Stamp**: When alternative version was created
5. **Purpose Statement**: Why this version exists

### Canonical Version Authority
- The `/book/` directory in main branch is the official canonical version
- All chapter numbers in canonical version are authoritative
- Alternative versions may not claim chapter numbers used in canonical version
- SUMMARY.md in canonical version is the definitive table of contents

## Folder Guidelines

### `/chapters/`
**Purpose**: Final, polished chapter content ready for publication

**Rules**:
- Only complete, well-edited chapters
- Follow consistent formatting and structure
- Include integrated case studies within chapters
- Use standard chapter numbering (match book outline)

**Do NOT include**:
- Draft content or works-in-progress
- Multiple versions of same chapter
- Outline or planning documents

### `/resources/`
**Purpose**: Supporting materials for book development

**Subfolders**:
- `/images/` - Diagrams, charts, company logos, author photos
- `/templates/` - Standardized formats for chapters, case studies
- `/research/` - Background materials, data, interview transcripts

### `/drafts/`
**Purpose**: Work-in-progress and developmental content

**Subfolders**:
- `/outlines/` - Chapter planning, book structure documents
- `/fragments/` - Partial content, ideas, rough sections
- `/archive/` - Old versions, discarded content (don't delete, move here)

### Root Directory
**Keep minimal**: Only essential navigation and reference files
- `README.md` - Project overview and current status
- `FOLDER_STRUCTURE.md` - This organizational guide
- `case_studies.md` - Master case study reference

## Content Organization Principles

### Chapter Development Workflow
1. **Planning**: Create outline in `/drafts/outlines/`
2. **Drafting**: Write initial version in `/drafts/fragments/`
3. **Integration**: Incorporate case studies and polish
4. **Finalization**: Move completed chapter to `/chapters/`
5. **Archive**: Move old versions to `/drafts/archive/`

### Case Study Integration
- **Primary Location**: Within relevant chapters
- **Reference**: Maintain master list in `case_studies.md`
- **Avoid Duplication**: Don't repeat full case studies across chapters
- **Cross-Reference**: Link between chapters when case studies relate

### Version Control
- **Keep Clean Main**: Only final versions in main folders
- **Archive Old Versions**: Move to `/drafts/archive/` with date suffix
- **Use Descriptive Names**: `chapter_18_v2_2024-01-15.md`
- **Document Changes**: Note major revisions in file or commit messages

## Quality Standards

### Chapter Requirements
- **Consistent Structure**: Introduction, main sections, key takeaways
- **Integrated Case Studies**: 3-5 relevant examples per chapter
- **Professional Formatting**: Proper markdown, consistent style
- **Word Count**: Target 4,000-6,000 words per chapter
- **Cross-References**: Link to related chapters and case studies

### Case Study Standards
- **Company Snapshot**: Basic facts and context
- **Key Innovation**: What makes them notable
- **Lessons Learned**: Actionable insights for founders
- **Zero to Three Relevance**: How they illustrate framework stages
- **Geographic Diversity**: Balance across regions and markets

### File Quality Checklist
- [ ] Follows naming conventions
- [ ] Proper folder location
- [ ] Consistent formatting
- [ ] No duplicate content
- [ ] Links work correctly
- [ ] Integrated case studies
- [ ] Professional writing quality

## Expansion Guidelines

### Adding New Chapters
1. Create outline in `/drafts/outlines/outline_chapter_XX.md`
2. Draft content in `/drafts/fragments/`
3. Select and integrate relevant case studies
4. Polish and edit for consistency
5. Move final version to `/chapters/chapter_XX.md`
6. Update `README.md` with new chapter

### Adding New Case Studies
1. Research and draft in `/drafts/fragments/`
2. Follow standard case study format
3. Add to master `case_studies.md` compendium
4. Integrate into relevant chapters
5. Ensure geographic and sector diversity

### Managing Resources
- **Images**: Optimize file sizes, use descriptive names
- **Research**: Date and source all materials
- **Templates**: Keep updated as formats evolve
- **Archive**: Regularly clean up old drafts

## Collaboration Guidelines

### For Contributors
- **Follow Structure**: Use designated folders and naming
- **Check Duplicates**: Avoid creating redundant content
- **Maintain Quality**: Meet writing and formatting standards
- **Document Changes**: Clear commit messages and change notes

### For Editors
- **Work in Drafts**: Don't edit final chapters directly
- **Track Versions**: Archive edited versions with dates
- **Maintain Links**: Check cross-references after changes
- **Update Index**: Keep README.md current

## Maintenance Schedule

### Weekly
- [ ] Review `/drafts/` folder for completed content to promote
- [ ] Check for orphaned files or broken links
- [ ] Archive old draft versions

### Monthly
- [ ] Update folder structure if needed
- [ ] Review case study balance (geographic, sector, outcome)
- [ ] Clean up `/resources/` folder organization

### Before Publication
- [ ] Final folder cleanup and organization
- [ ] Archive all draft materials
- [ ] Verify all links and references
- [ ] Create publication-ready structure

---

## Quick Reference Commands

### Create New Chapter
```bash
# Create outline
touch /drafts/outlines/outline_chapter_XX.md

# Create draft
touch /drafts/fragments/chapter_XX_draft.md

# When ready, move to final
mv /drafts/fragments/chapter_XX_final.md chapters/chapter_XX.md
```

### Archive Old Version
```bash
# Archive with date
mv chapters/chapter_XX.md drafts/archive/chapter_XX_$(date +%Y%m%d).md
```

### Check Structure
```bash
# View current structure
tree -L 3

# Count chapters
ls chapters/ | wc -l
```

This folder structure ensures the "Zero to Three" project remains organized, scalable, and professional as it grows from the current 2 chapters to a complete book.