# GitHub 上传指南

## 方案一：使用 Git 命令行（推荐）

### 步骤 1：打开命令行工具
打开 PowerShell 或 Git Bash，进入网站目录：
```bash
cd d:/ITO产品手册/website
```

### 步骤 2：初始化仓库（如尚未初始化）
```bash
git init
```

### 步骤 3：添加远程仓库
```bash
git remote add origin https://github.com/Mightymojoy/-product.git
```

### 步骤 4：添加并提交文件
```bash
git add .
git commit -m "Initial commit: ITO产品手册网站"
```

### 步骤 5：推送到 GitHub
```bash
git branch -M main
git push -u origin main
```

---

## 方案二：使用 GitHub 网页上传

### 步骤 1：访问仓库
打开浏览器访问：https://github.com/Mightymojoy/-product

### 步骤 2：上传文件
1. 点击 "Add file" 按钮
2. 选择 "Upload files"
3. 拖拽以下文件到上传区域：
   - `index.html`
   - `ito-care.html`
   - `README.md`
   - `.gitignore`
4. 填写 commit 描述
5. 点击 "Commit changes"

### 步骤 3：启用 GitHub Pages（重要！）
1. 进入仓库 Settings
2. 左侧菜单选择 "Pages"
3. Source 选择 "Deploy from a branch"
4. Branch 选择 "main" 和 "/ (root)"
5. 点击 "Save"

### 步骤 4：等待部署
等待 1-2 分钟，网站将自动部署到：
```
https://Mightymojoy.github.io/-product
```

---

## 上传到仓库的文件

需要上传的文件：
- `index.html` - 主页面
- `ito-care.html` - ITO CARE服务页面
- `README.md` - 项目说明
- `.gitignore` - Git忽略规则

---

## 注意事项

1. **不要上传大文件**：product_images 文件夹（约40MB+）已通过 .gitignore 忽略
2. **GitHub Pages 限制**：免费版有 1GB 存储限制
3. **图片加载**：产品图片已嵌入HTML，可正常显示
