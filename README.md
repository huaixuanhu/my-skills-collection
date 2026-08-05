# My Skills Collection

这是个人自创 AI skills 的 canonical repository（权威仓库）。`skills/` 中的版本同时服务于本地开发、Git 历史、GitHub 备份和 Codex 安装，避免多个独立副本逐渐漂移。

仓库保持 private（私有）。skill 运行目录只保留执行所需文件；测试、安装工具和版本历史位于外层，不会随 `SKILL.md` 一起载入模型上下文。

## Repository Layout

```text
skills/<skill-name>/          canonical skill package
tests/<skill-name>/           skill-specific regression tests
releases/<skill-name>/        concise version evidence
scripts/manage_skills.py      validate, install, and link checks
.github/workflows/            GitHub validation
AGENTS.md                     durable collaboration rules
CHANGELOG.md                  cross-skill version history
```

当前包含：

| Skill | Version | Status |
| --- | --- | --- |
| `human-ai-governance` | `0.5.1` | canonical and validated |

## Local Workflow

首次建立本地 virtual environment（虚拟环境）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

运行全部仓库校验：

```bash
.venv/bin/python scripts/manage_skills.py validate
```

把一个 skill 安装为指向 canonical source（权威源码）的 symlink（符号链接）：

```bash
.venv/bin/python scripts/manage_skills.py install human-ai-governance --replace
```

检查安装是否仍指向当前仓库：

```bash
.venv/bin/python scripts/manage_skills.py check human-ai-governance
```

默认安装根目录是 `${CODEX_HOME}/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。被替换且内容完全一致的实体目录会先移动到 `${CODEX_HOME}/skill-backups` 或 `~/.codex/skill-backups`。

## Change Workflow

1. 只修改 `skills/<skill-name>/` 中的 canonical source。
2. 同步更新对应测试和根 `CHANGELOG.md`。
3. 为 material release（实质版本）更新 `releases/<skill-name>/v<version>.md`。
4. 运行 aggregate validation（聚合校验）和可用的官方 skill validator。
5. 检查 diff 后 commit、push。
6. 为已通过验证的版本创建 `<skill-name>-v<version>` tag。

新增 skill 时，建立 `skills/<name>/SKILL.md`；管理脚本会自动发现并验证它。只有在该 skill 需要专门回归时才创建 `tests/<name>/`。
