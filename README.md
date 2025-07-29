# # ai-readme-templates
# 
# 此仓库用于集中管理不同框架的 Cursor 规则模板（如 **Laravel**、**Next.js**、**Flutter**）以及自动同步这些规则到各项目的 Python 脚本。通过统一的规则模板和脚本，可以在多台电脑或多个项目之间保持一致的编码规范和项目结构，无需重复粘贴规则。
# 
# ## 📂 仓库结构
# 
# - `laravel_rule.md`、`nextjs15_rule.md`、`flutter_rule.md`：对应各框架的规则模板，内容请根据自己的需求编写。
# - `sync_ai_rules.py`：同步脚本，负责将指定的规则模板复制到每个 Laravel 项目的 `.cursor/rules` 文件中。
# - `generate_laravel_projects.py`：辅助脚本，用于扫描指定目录并生成一个包含所有 Laravel 项目路径的 JSON 文件，供同步脚本使用（可选）。
# 
# ## 🚀 使用方法
# 
# 1. **准备规则模板**
# 
#    在仓库根目录编写或更新你的规则模板，例如 `laravel_rule.md`。这个文件将作为同步脚本的来源内容。
# 
# 2. **生成 Laravel 项目清单（可选）**
# 
#    如果想提前确定要同步的项目列表，可以运行 `generate_laravel_projects.py`：
#    ```bash
#    python generate_laravel_projects.py /Users/maxxi/Documents/www /Users/maxxi/Documents/www/laravel_projects.json
#    ```
#    这会扫描 `/Users/maxxi/Documents/www` 目录下所有包含 `artisan` 文件的目录，并将其绝对路径写入 `laravel_projects.json`。
# 
# 3. **同步规则到项目**
# 
#    运行 `sync_ai_rules.py` 将模板复制到每个项目的 `.cursor/rules`：
#    ```bash
#    # 方式一：直接扫描目录，自动检测 Laravel 项目
#    python sync_ai_rules.py /Users/maxxi/Documents/www /Users/maxxi/Documents/ai-readme-templates/laravel_rule.md
# 
#    # 方式二：使用预生成的项目清单
#    python sync_ai_rules.py /Users/maxxi/Documents/www /Users/maxxi/Documents/ai-readme-templates/laravel_rule.md /Users/maxxi/Documents/www/laravel_projects.json
#    ```
#    - 第一个参数：项目根目录。
#    - 第二个参数：规则模板文件路径。
#    - 第三个参数（可选）：JSON 清单文件路径。如果提供，则脚本根据清单中的路径同步；如果省略，则自动遍历目录并检测 `artisan`。
# 
#    脚本运行后，会在每个检测到的 Laravel 项目目录下创建 `.cursor` 文件夹（如果不存在），并写入 `.cursor/rules` 文件。
# 
# 4. **更新模板与重新同步**
# 
#    当你修改了 `laravel_rule.md` 或其他规则模板时，只需重新运行同步脚本，所有项目的规则将自动更新。这样即便换新电脑，只需拉取此仓库并运行脚本即可获得最新规则。
# 
# ## 📄 许可证
# 
# 根据你的开源需求选择合适的许可证，例如 MIT 或 Apache-2.0。如果仅内部使用，可以保持私有或使用公司内部许可证。
