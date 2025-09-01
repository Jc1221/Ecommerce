# Git Upload Instructions

## Step 1: Initialize Git Repository

```bash
cd "c:\Users\jeffr\Desktop\Software P\ecommerce"
git init
```

## Step 2: Add Remote Repository

```bash
git remote add origin https://github.com/Jc1221/Ecommerce.git
```

## Step 3: Add All Files

```bash
git add .
```

## Step 4: Create Initial Commit

```bash
git commit -m "Initial commit: Django ecommerce platform with role-based user system

Features:
- Multi-role user system (Admin, Merchant, Customer)
- Merchant product management with CRUD operations
- Role-based navigation system
- Modern Bootstrap 4 UI
- Product catalog with search functionality
- Shopping cart and checkout process
- Order management and tracking
- Image upload for products
- Real-time merchant dashboard with statistics
- Enhanced security with permission-based access control

Technology Stack:
- Django 2.2.28
- Bootstrap 4
- FontAwesome icons
- jQuery 3.3.1
- SQLite/PostgreSQL support"
```

## Step 5: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## Alternative: If repository already exists and has content

If the repository already has files, use:

```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

## Verify Upload

After pushing, check:
1. Go to https://github.com/Jc1221/Ecommerce
2. Verify all files are uploaded
3. Check that README.md displays correctly
4. Ensure .gitignore is working (no __pycache__ or db.sqlite3 files)

## Quick Commands Summary

```bash
cd "c:\Users\jeffr\Desktop\Software P\ecommerce"
git init
git remote add origin https://github.com/Jc1221/Ecommerce.git
git add .
git commit -m "Initial commit: Django ecommerce platform with role-based user system"
git branch -M main
git push -u origin main
```