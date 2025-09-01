# User Roles and Merchant System

This ecommerce platform now supports three distinct user roles:

## User Roles

### 1. **Regular Users (Customers)**
- Can browse and purchase products
- Manage their cart and orders
- Update shipping/billing addresses
- Register at: `/register/`

### 2. **Merchants**
- All customer capabilities
- Can create, edit, and manage their own products
- Can set prices and upload product images
- Access to merchant dashboard at: `/merchants/`
- Register at: `/register/merchant/`

### 3. **Admin Users**
- Full system access
- Can manage all users, products, and orders
- Access Django admin panel at: `/admin/`
- Separate from merchant privileges

## Getting Started

### For Merchants
1. **Register as Merchant**: Visit `/register/merchant/` or click "Become Merchant" in the navigation
2. **Login**: Use your credentials to login
3. **Access Dashboard**: Navigate to `/merchants/` or use the "Merchant" dropdown in navigation
4. **Manage Products**: Create, edit, delete, and toggle visibility of your products

### For Admins
1. **Create Admin**: Use the management command:
   ```bash
   python manage.py create_admin admin@example.com --full_name "Admin Name" --password your_password
   ```
2. **Access Admin Panel**: Visit `/admin/` and login with admin credentials

## Management Commands

### Create a Merchant User
```bash
python manage.py create_merchant merchant@example.com --full_name "Merchant Name" --password merchant123
```

### Create an Admin User
```bash
python manage.py create_admin admin@example.com --full_name "Admin Name" --password admin123
```

## Features

### Merchant Dashboard (`/merchants/`)
- Overview of total and active products
- Quick actions to add new products
- Recent products list
- Access to product management

### Product Management (`/merchants/products/`)
- List all merchant's products
- Create new products with form validation
- Edit existing products (only own products)
- Delete products with confirmation
- Toggle product active/inactive status
- Upload product images

### Security Features
- **Role-based Access Control**: Merchants can only manage their own products
- **Permission Decorators**: `@merchant_required` ensures only merchants access merchant views
- **Admin Separation**: Admin accounts are completely separate from merchant accounts
- **Product Ownership**: Products are tied to specific merchants

## Database Changes

### User Model Extensions
- Added `merchant` boolean field to User model
- Updated UserManager with `create_merchant()` method
- Added `is_merchant` property

### Product Model Extensions
- Added `merchant` ForeignKey field linking products to merchants
- Products are now owned by specific merchants
- Admin users can still manage all products through Django admin

## Navigation Updates
- Merchant dropdown appears for logged-in merchants
- "Become Merchant" link for guest users
- Role-specific navigation based on user permissions

## Templates
- Responsive merchant dashboard
- Product management interface
- Form-based product creation/editing
- Confirmation dialogs for product deletion
- Bootstrap 4 styled components

## Notes
- Existing products will have `merchant` field as `null` initially
- Admin users can assign merchants to existing products through Django admin
- All merchant operations are logged and tracked
- Products without merchants can still be managed by admin users