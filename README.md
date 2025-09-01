# Django Ecommerce Platform

A full-featured ecommerce platform built with Django, featuring role-based user management, merchant capabilities, and comprehensive product management.

## 🚀 Features

### 👥 **Multi-Role User System**
- **Customers**: Browse, search, and purchase products
- **Merchants**: Upload/modify products, manage inventory, set prices
- **Admins**: Full system control, separate from merchant accounts

### 🏪 **Merchant Features**
- Merchant registration and dashboard
- Product CRUD operations (Create, Read, Update, Delete)
- Product image upload and management
- Price and inventory management
- Product status control (active/inactive/featured)
- Real-time statistics dashboard

### 🛒 **Ecommerce Features**
- Product catalog with search functionality
- Shopping cart and checkout process
- Order management and tracking
- Address management for shipping/billing
- Guest checkout capabilities

### 🎨 **Modern UI/UX**
- Role-based navigation system
- Bootstrap 4 responsive design
- FontAwesome icons integration
- Dynamic role indicators
- Mobile-friendly interface

## 🛠️ **Technology Stack**

- **Backend**: Django 2.2.28, Python 3.8+
- **Frontend**: HTML5, CSS3, Bootstrap 4, jQuery 3.3.1
- **Database**: SQLite (development), PostgreSQL/MySQL (production)
- **Icons**: FontAwesome
- **File Uploads**: Pillow for image processing

## 📦 **Installation & Setup**

### **Prerequisites**
- Python 3.8 or higher
- pip package manager
- Git

### **Quick Start**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jc1221/Ecommerce.git
   cd Ecommerce
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Navigate to project directory**
   ```bash
   cd ecommerce
   ```

4. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create test accounts**
   ```bash
   # Create admin account
   python manage.py create_admin admin@example.com --full_name "Admin User" --password admin123
   
   # Create merchant account
   python manage.py create_merchant merchant@example.com --full_name "Test Merchant" --password merchant123
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - Merchant dashboard: http://127.0.0.1:8000/merchants/

## 👤 **Test Accounts**

### **Admin Account**
- Email: `admin@example.com`
- Password: `admin123`
- Access: Full system administration

### **Merchant Account**
- Email: `merchant@example.com`
- Password: `merchant123`
- Access: Product management and merchant dashboard

### **Customer Registration**
- Register at: http://127.0.0.1:8000/register/
- Merchant registration: http://127.0.0.1:8000/register/merchant/

## 🧭 **Navigation Guide**

### **Admin Users**
- Access Django Admin for full system control
- Manage all users, products, and orders
- System-wide configuration and monitoring

### **Merchants**
- Dashboard with product statistics
- Create and manage products
- Upload product images and set prices
- Track product performance

### **Customers**
- Browse product catalog
- Add items to cart and checkout
- Manage profile and order history
- Track orders and manage addresses

## 📁 **Project Structure**

```
ecommerce/
├── accounts/           # User authentication and management
├── addresses/          # Address management
├── billing/            # Billing profiles
├── carts/              # Shopping cart functionality
├── merchants/          # Merchant-specific features
├── orders/             # Order processing
├── products/           # Product catalog
├── search/             # Search functionality
├── tags/               # Product tagging
├── templates/          # HTML templates
├── static_my_proj/     # Static files (CSS, JS, images)
└── ecommerce/          # Project settings and configuration
```

## 🔧 **Key Features**

### **Role-Based Access Control**
- Dynamic navigation based on user roles
- Permission-based view access
- Visual role indicators

### **Merchant Management**
- Dedicated merchant registration
- Product upload and management
- Real-time dashboard statistics
- Inventory control

### **Enhanced User Experience**
- Responsive design for all devices
- Intuitive navigation system
- Search and filter capabilities
- Modern UI with Bootstrap 4

## 🚀 **Deployment**

### **Production Setup**
1. Set `DEBUG = False` in settings.py
2. Configure production database (PostgreSQL/MySQL)
3. Set up static file serving (Nginx/Apache)
4. Use WSGI server (Gunicorn/uWSGI)
5. Configure environment variables for sensitive data

### **Environment Variables**
```bash
export SECRET_KEY="your-secret-key"
export DEBUG=False
export DATABASE_URL="your-database-url"
```

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 **License**

This project is open source and available under the MIT License.

## 🆘 **Support**

For support and questions:
- Create an issue on GitHub
- Check the documentation in the project files
- Review the code comments for implementation details

## 🔄 **Updates**

- ✅ Multi-role user system
- ✅ Merchant product management
- ✅ Role-based navigation
- ✅ Modern UI/UX improvements
- ✅ Enhanced security features

---

**Built with ❤️ using Django and Bootstrap**