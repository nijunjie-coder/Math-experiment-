# 数学计算练习：3×3 矩阵的行列式

使用 Python 和 SymPy（符号数学计算库）计算符号矩阵的行列式，并验证一个已知答案。

## 文件用途

| 文件 | 用途 |
| --- | --- |
| `determinant.py` | 计算符号行列式，代入数值并检查已知答案。 |
| `requirements.txt` | 声明需要安装的 SymPy 版本。 |
| `.gitignore` | 让 Git 忽略虚拟环境和 Python 缓存。 |
| `README.md` | 项目说明、运行方法和保存步骤。 |

## 如何运行

需要 Python 3。在终端进入项目文件夹，然后依次运行（Codex 云环境、Linux 或 macOS）：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python determinant.py
```

Windows PowerShell 中，前两条改为 `py -m venv .venv` 和 `.venv\Scripts\Activate.ps1`；后两条相同。

以后打开新终端时，进入项目文件夹并激活虚拟环境即可，不需要每次重新安装依赖。

## 计算与验证

符号矩阵：

```text
[a b c]
[d e f]
[g h i]
```

行列式为：

```text
a*e*i - a*f*h - b*d*i + b*f*g + c*d*h - c*e*g
```

验证使用：

```text
[1 2 3]
[0 4 5]
[5 0 1]
```

按第一行展开，已知答案为：

```text
1×(4×1-5×0) - 2×(0×1-5×5) + 3×(0×0-4×5)
= 4 + 50 - 60
= -6
```

程序将这些数值代入符号结果，并直接计算数值矩阵的行列式，检查两者是否都等于 `-6`。
成功时输出 `验证通过：行列式 = -6（已知答案为 -6）`；失败时抛出异常，以非零状态退出。

## 如何保存到 GitHub

工作区中的修改不会自动上传到 GitHub。“提交”（commit）创建本地版本，“推送”（push）将版本上传。

在项目文件夹的终端中执行：

```bash
git status
git diff
git add determinant.py requirements.txt .gitignore README.md
git commit -m "添加 SymPy 矩阵行列式练习"
git branch --show-current
git push -u origin HEAD
```

推送后，在 GitHub 打开 `nijunjie-coder/Math-experiment-`，选择上面命令显示的分支即可看到文件。
如果当前分支不是 `main`，可通过 GitHub 的 **Compare & pull request** 创建合并请求，检查后合并到 `main`。如果 Codex 界面提供“创建 PR”按钮，也可使用它。

如果提交时提示缺少作者信息，按照 Git 的提示设置自己的 `user.name` 和 `user.email` 后重试。若推送提示权限不足，请检查 GitHub 连接的写入权限；不要把密码或令牌写进代码。
