class SessionManager:
    """إدارة بيانات الجلسة للمستخدم الحالي"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.user_data = {}
        return cls._instance

    def set_user_data(self, card_uid, student_code, name, email, password):
        """حفظ بيانات المستخدم"""
        self.user_data = {
            'card_uid': card_uid,
            'student_code': student_code,
            'name': name,
            'email': email,
            'password': password
        }
        print(f"✅ تم حفظ بيانات الجلسة: {self.user_data}")

    def get_user_data(self):
        """الحصول على بيانات المستخدم"""
        return self.user_data

    def get_card_uid(self):
        """الحصول على Card UID"""
        return self.user_data.get('card_uid', '')

    def get_student_code(self):
        """الحصول على كود الطالب"""
        return self.user_data.get('student_code', '')

    def get_name(self):
        """الحصول على اسم الطالب"""
        return self.user_data.get('name', '')

    def get_email(self):
        """الحصول على الإيميل"""
        return self.user_data.get('email', '')

    def get_password(self):
        """الحصول على كلمة المرور"""
        return self.user_data.get('password', '')

    def clear_session(self):
        """مسح بيانات الجلسة (تسجيل خروج)"""
        self.user_data = {}
        print("✅ تم مسح بيانات الجلسة")

    def is_logged_in(self):
        """التحقق من تسجيل الدخول"""
        return bool(self.user_data.get('card_uid'))