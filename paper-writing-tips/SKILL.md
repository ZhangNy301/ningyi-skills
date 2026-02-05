---
name: paper-writing-tips
description: Academic paper writing guide for ML/NLP researchers. Use when the user is writing, reviewing, or polishing academic papers (especially ML/NLP conference papers), needs help with LaTeX formatting, formula notation, table/figure design, English writing style, citation formats, or pre-submission checks. Triggers on keywords like paper writing, LaTeX tips, formula notation, academic writing, conference submission, rebuttal, or any paper-related questions.
---

# Paper Writing Tips

This skill provides comprehensive guidance for writing high-quality academic papers, especially for ML/NLP conferences. It covers LaTeX formatting, mathematical notation, figure/table design, English writing style, and pre-submission checklists.

## When to Use

- Writing or reviewing academic papers
- Formatting LaTeX documents
- Designing figures and tables
- Polishing English writing
- Preparing paper submissions
- Checking final drafts before submission

## Core Guidelines

### Formula Notation

1. **Scalars**: Use lowercase Latin letters. Replace `l` with `\ell` to avoid confusion with `1`.
2. **Structured values**: Use `\boldsymbol` for sequences, trees, graphs.
3. **Sets of structured values**: Use `\mathcal` (e.g., `\mathcal{D}` for dataset).
4. **Vectors**: Lowercase bold (`\mathbf` for Latin, `\boldsymbol` for Greek).
5. **Matrices**: Uppercase bold (`\mathbf` for Latin, `\boldsymbol` for Greek).
6. **Number fields/expectations**: Use `\mathbb` (e.g., `\mathbb{R}`, `\mathbb{E}`).
7. **Multi-letter variables**: Use `\textrm` or `\textit` (e.g., `\textrm{softmax}`).
8. **Functions**: Use built-in commands like `\arg`, `\max`, `\sin`, `\tanh`.
9. **Parentheses**: Use `\left` and `\right` for auto-sizing.
10. **Equation alignment**: Use `align` environment for multiple equations.
11. **Numbering**: Only number equations that are referenced; use `\nonumber` for others.

### Writing Style

1. **Avoid contractions**: Write "do not" instead of "don't".
2. **Avoid possessive 's**: Use "of" phrases instead.
3. **Latin abbreviations**:
   - `e.g.,` = for example
   - `i.e.,` = that is
   - `et al.` = and others
   - `etc.` = and others (not for people)
4. **Quotation marks**: Use `` and '' for English quotes, not "".
5. **Non-breaking spaces**: Use `~` before citations/refs (e.g., `Figure~\ref{fig:1}`).
6. **URLs**: Use `\url{}` with `\usepackage{hyperref}`.
7. **Tense**: Use present tense primarily.

### Tables and Figures

1. **Tables**: Use `booktabs` package with `\toprule`, `\midrule`, `\bottomrule`.
2. **Avoid vertical lines**: Use "three-line table" style.
3. **Sizing**: Use `\small`, `\scriptsize`, `\setlength{\tabcolsep}{}` for adjustments.
4. **Figures**: Use vector graphics (PDF format).
5. **Font size**: Figure text should be between caption size and body text size.
6. **Color**: Design for black-and-white printing; use line styles, not just colors.
7. **Consistency**: Same modules use same colors; arrows flow in same direction.

### Word Choice

1. **Hyphenated words**: Last word determines part of speech (noun=adjective, verb=verb).
2. **Common mistakes**:
   - "First" (not Firstly), "Second" (not Secondly)
   - "training" (noun), "test" (noun), not "testing"
3. **Abbreviations**: Define on first use; match established conventions.
4. **Articles**: `a`/`an` by sound not letter ("an LSTM", "a U").
5. **Avoid absolutes**: Use "straightforward" not "obvious", "generally" not "always".
6. **Be specific**: Avoid vague words like "better", "meaning", "semantic".

### Sentence Structure

1. **One idea per sentence**: Prefer simple sentences over complex ones.
2. **Minimize pronouns**: Use model names instead of "it", "they".
3. **Avoid vague labels**: Explain what improved and why.
4. **Separate concepts**: Don't mix observations, hypotheses, methods, and results.

### Citations

1. **In-text vs parenthetical**:
   - ACL/NAACL/EMNLP: `\citet{}` for in-text
   - COLING: `\newcite{}`
   - AAAI/IJCAI: `\citeauthor{} \shortcite{}`
   - IEEE: `\citeauthor{}~(\citeyear{})`
2. **Prefer published versions** over arXiv.
3. **Consistency**: Same format for all entries (venue abbreviations, dates, etc.).
4. **Tools**: Use SimBiber for venue abbreviations, Rebiber for consistent bib entries.

### Pre-submission Checklist

1. **Anonymity**: No author/institution info in paper or code.
2. **Page limit**: Check against conference requirements.
3. **Title/abstract**: Match submission system entries.
4. **Code/data**: Remove hardcoded paths, hidden folders (.git).
5. **Grammar check**: Use Grammarly or Writefull.
6. **Consistency**: Model names (BERT not Bert), title capitalization.
7. **Figures**: Vector graphics, consistent fonts, appropriate sizing.
8. **Equations**: Punctuation as part of sentences.
9. **References**: No duplicate arXiv + published versions.
10. **Backup**: Version files with dates; submit early to avoid server issues.

## Reference Materials

For detailed examples and LaTeX code, see [references/detailed_guide.md](references/detailed_guide.md).

For common LaTeX templates and snippets, see [references/latex_snippets.md](references/latex_snippets.md).
