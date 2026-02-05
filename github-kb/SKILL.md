---
name: github-kb
description: |
  管理本地 GitHub 仓库知识库，支持仓库克隆、索引管理和查询分析。
  当用户提到以下任一内容时触发：
  - "github"、"repo"、"仓库"、"repository"
  - 提及下载/克隆仓库
  - 询问关于某个仓库的问题
  - 需要搜索 GitHub issue/PR/repository
  优先在本地目录 `/Users/ningyizhang/github` 查找用户提到的仓库，
  并使用 gh 命令或 curl 在 GitHub 上搜索信息。
---

# GitHub 知识库管理

## 本地仓库目录

本地 GitHub 仓库根目录: `/Users/ningyizhang/github`

该目录下的所有仓库在 @/Users/ningyizhang/github/CLAUDE.md 中有索引记录。

## 核心功能

### 1. 下载/克隆仓库

当用户要求下载仓库时：

```bash
# 克隆到本地目录
cd /Users/ningyizhang/github
git clone <repo-url>

# 更新 CLAUDE.md 索引
cd <repo-name>
echo "- $(basename $PWD): $(git remote get-url origin | sed 's/.*github.com\///') - $(head -20 README.md 2>/dev/null | grep -i 'description\|简介\|about' | head -1 || echo '待补充摘要')" >> ../CLAUDE.md
```

### 2. 查询本地仓库

当用户询问某个仓库时，优先在本地查找：

```bash
# 检查仓库是否存在
ls /Users/ningyizhang/github/<repo-name>

# 读取仓库 README
cat /Users/ningyizhang/github/<repo-name>/README.md

# 查看仓库结构
find /Users/ningyizhang/github/<repo-name> -maxdepth 2 -type f | head -30
```

### 3. GitHub 搜索

优先尝试使用 `gh` 命令，如果不可用则使用 `curl` 调用 GitHub API。

#### 检查 gh 可用性

```bash
# 检查 gh 是否安装且已登录
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    USE_GH=true
else
    USE_GH=false
fi
```

#### 搜索仓库

**使用 gh:**
```bash
gh search repos <keyword> --limit 10
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/search/repositories?q=<keyword>&sort=stars&order=desc&per_page=10" | jq -r '.items[] | "\(.full_name): \(.description) [⭐\(.stargazers_count)]"'
```

#### 搜索 Issues

**使用 gh:**
```bash
gh search issues <keyword> --repo <owner/repo> --limit 10
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/search/issues?q=<keyword>+repo:<owner/repo>+is:issue&sort=updated&order=desc&per_page=10" | jq -r '.items[] | "#\(.number): \(.title) [\(.state)]"'
```

#### 搜索 PRs

**使用 gh:**
```bash
gh search prs <keyword> --repo <owner/repo> --limit 10
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/search/issues?q=<keyword>+repo:<owner/repo>+is:pr&sort=updated&order=desc&per_page=10" | jq -r '.items[] | "#\(.number): \(.title) [\(.state)]"'
```

#### 查看仓库信息

**使用 gh:**
```bash
gh repo view <owner/repo>
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/repos/<owner/repo>" | jq -r '{name: .name, description: .description, stars: .stargazers_count, forks: .forks_count, updated: .updated_at}'
```

#### 查看 Issue 列表

**使用 gh:**
```bash
gh issue list --repo <owner/repo> --limit 20
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/repos/<owner/repo>/issues?state=open&per_page=20" | jq -r '.[] | "#\(.number): \(.title) [\(.state)]"'
```

#### 查看 PR 列表

**使用 gh:**
```bash
gh pr list --repo <owner/repo> --limit 20
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/repos/<owner/repo>/pulls?state=open&per_page=20" | jq -r '.[] | "#\(.number): \(.title) [\(.state)]"'
```

#### 查看最近提交

**使用 gh:**
```bash
gh api repos/<owner/repo>/commits --jq '.[] | "\(.sha[:7]): \(.commit.message | split("\n")[0])"' | head -10
```

**使用 curl (备选):**
```bash
curl -s "https://api.github.com/repos/<owner/repo>/commits?per_page=10" | jq -r '.[] | "\(.sha[:7]): \(.commit.message | split("\n")[0])"'
```

## 工作流程

### 用户提及仓库时

1. **检查本地是否存在**
   - 如果存在：读取 README 和关键文件，分析回答
   - 如果不存在：询问是否需要克隆，或使用 gh/curl 搜索远程信息

2. **选择查询方式**
   - 先检查 `gh` 是否可用且已登录
   - 如果不可用，自动切换到 `curl` + GitHub API

3. **更新索引**
   - 克隆新仓库后，更新 CLAUDE.md
   - 定期同步仓库摘要

### 用户要求下载时

1. 解析仓库 URL 或名称
2. 执行 `git clone` 到 `/Users/ningyizhang/github`
3. 读取 README 生成摘要
4. 更新 CLAUDE.md 索引文件
5. 向用户确认完成

## 目录检查

如果 `/Users/ningyizhang/github` 目录不存在：
1. 询问用户正确的本地仓库路径
2. 更新本 SKILL.md 中的路径配置
3. 在新位置创建 CLAUDE.md

## 当前索引

参见 @/Users/ningyizhang/github/CLAUDE.md 获取完整仓库列表和摘要。
