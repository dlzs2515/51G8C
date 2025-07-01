import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# 用户数据文件路径
USER_DATA_FILE = 'usersdata.json'

def load_users():
    """从JSON文件加载用户数据"""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """保存用户数据到JSON文件"""
    with open(USER_DATA_FILE, 'w') as f:
        json.dump(users, f)

# 上传文件夹配置
UPLOAD_FOLDER = 'static/userfiles'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    username = session.get('username', '游客')
    return render_template('index.html', username=username)

# 登录路由
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()  # 从文件加载用户数据
        # 简单的用户验证（实际应用中应使用数据库）
        if username in users and users[username] == password:
            session['username'] = username
            flash('登录成功！')
            return redirect(url_for('index'))
        flash('用户名或密码错误！')
    return render_template('login.html')

# 注册路由
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()  # 从文件加载用户数据
        if username in users:
            flash('用户名已存在！')
        else:
            users[username] = password
            save_users(users)  # 保存到文件
            session['username'] = username
            # 创建用户文件夹
            user_folder = os.path.join(app.config['UPLOAD_FOLDER'], username)
            os.makedirs(user_folder, exist_ok=True)
            flash('注册成功！')
            return redirect(url_for('index'))
    return render_template('register.html')

# 注销路由
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('您已注销。')
    return redirect(url_for('index'))

# 文件上传路由
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'username' not in session or session['username'] == '游客':
        flash('请先登录！')
        return redirect(url_for('login'))
    
    if 'file' not in request.files:
        flash('没有文件部分')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('未选择文件')
        return redirect(request.url)
    
    if file and file.filename.endswith('.cpp'):
        username = session['username']
        filename = secure_filename(file.filename)
        user_folder = os.path.join(app.config['UPLOAD_FOLDER'], username)
        os.makedirs(user_folder, exist_ok=True)
        file.save(os.path.join(user_folder, filename))
        flash('文件上传成功！')
        return redirect(url_for('index'))
    else:
        flash('只允许上传.cpp文件！')
    return redirect(request.url)

# 上传文件页面路由
@app.route('/upload_page', methods=['GET'])
def upload_page():
    # 检查用户是否登录
    if 'username' not in session or session['username'] == '游客':
        flash('请先登录！')
        return redirect(url_for('login'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True,port=6666)