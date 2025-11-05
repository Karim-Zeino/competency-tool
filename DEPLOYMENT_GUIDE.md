# Competency Assessment Web App - Setup Guide

## 📦 What You Get

This package includes:
1. **Flexible Python Script** - For command-line processing (works with any questionnaire)
2. **Web Application** - User-friendly interface for your client

---

## 🚀 Option 1: Flexible Python Script (Recommended for You)

### Setup
```bash
pip install pandas
```

### Usage
The script automatically detects question columns (Q1, Q2, etc.) so it works with ANY questionnaire!

**Method 1 - Default file names:**
```bash
python competency_data_merge_flexible.py
```
(Uses: csv1_raw_data.csv and csv2_desired_state_mapping.csv)

**Method 2 - Custom file names:**
```bash
python competency_data_merge_flexible.py sales_raw.csv sales_desired.csv sales_output.csv
```

### Benefits
✅ Works with different questionnaires automatically
✅ No code changes needed between departments
✅ Detailed error reporting
✅ Progress tracking

---

## 🌐 Option 2: Web Application (For Your Client)

### Local Setup (Run on Your Computer)

1. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the app:**
```bash
python app.py
```

3. **Open in browser:**
```
http://localhost:5000
```

### How Your Client Uses It

1. Open the web page
2. Select department from dropdown:
   - Sales
   - Application Engineering
   - Commercial Operations
3. Upload CSV 1 (raw data)
4. Upload CSV 2 (desired state mapping)
5. Click "Process & Download"
6. Get the merged file instantly!

---

## ☁️ Option 3: Deploy Online (So Client Can Access Anywhere)

### A. Deploy to Heroku (Free Tier Available)

1. **Create a free Heroku account:** https://heroku.com

2. **Install Heroku CLI:**
   - Windows: Download from https://devcenter.heroku.com/articles/heroku-cli
   - Mac: `brew install heroku/brew/heroku`
   - Linux: `curl https://cli-assets.heroku.com/install.sh | sh`

3. **Create deployment files:**

Create `Procfile` (no extension):
```
web: python app.py
```

Create `runtime.txt`:
```
python-3.11.7
```

4. **Deploy:**
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-competency-tool

# Deploy
git init
git add .
git commit -m "Initial commit"
git push heroku main

# Open your app
heroku open
```

Your app will be at: `https://your-competency-tool.herokuapp.com`

### B. Deploy to PythonAnywhere (Easiest!)

1. **Create free account:** https://www.pythonanywhere.com

2. **Upload files:**
   - Upload all files through their web interface
   - Or use: `git clone your-repository-url`

3. **Setup web app:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Point to your `app.py` file

4. **Install dependencies:**
   Open Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```

5. **Reload web app**
   Your app will be at: `https://yourusername.pythonanywhere.com`

### C. Deploy to Render (Modern & Free)

1. **Create account:** https://render.com

2. **Create new Web Service:**
   - Connect your GitHub repository (or upload files)
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`

3. **Deploy!**
   Render automatically deploys your app.

---

## 🔐 Security Notes for Production

Before giving to client, update `app.py`:

```python
# Change this line:
app.secret_key = 'your-secret-key-change-this-in-production'

# To something secure like:
app.secret_key = 'mK8p#9Lq2$vN5wX7@zR4hT6jY3nB1gF0'
```

---

## 📝 Different Questionnaires for Different Departments

**No code changes needed!** The script automatically:
- Detects all Q1, Q2, Q3... columns
- Matches them between both files
- Works with different numbers of questions

So if:
- Sales has Q1-Q27
- Application Engineering has Q1-Q30
- Commercial Operations has Q1-Q25

The script handles all of them automatically! 🎉

---

## 🆘 Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### Port already in use
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed from 5000
```

### File upload fails
Check file size (max 16MB). To increase, change in `app.py`:
```python
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB
```

### CSV encoding issues
If you get encoding errors, modify `app.py`:
```python
csv1_data = pd.read_csv(raw_data_file, encoding='utf-8-sig')
csv2_data = pd.read_csv(desired_state_file, encoding='utf-8-sig')
```

---

## 🎯 Recommendation

**For You (Internal Use):**
Use the flexible Python script - it's fast and handles all departments automatically.

**For Your Client:**
Deploy the web app online (PythonAnywhere is easiest) so they can:
- Access from anywhere
- No technical knowledge needed
- No software installation required
- Professional interface

---

## 📧 Support

If you need help:
1. Check the error messages - they're detailed and helpful
2. Verify CSV files have correct column names
3. Ensure "Desired State" values in CSV1 match those in CSV2

---

## ✅ Quick Start Checklist

- [ ] Install Python 3.8+
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Test with sample data locally
- [ ] Deploy to web (if needed)
- [ ] Share link with client
- [ ] Celebrate! 🎉
