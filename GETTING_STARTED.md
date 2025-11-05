# 🚀 Getting Started - Competency Assessment Tool

## 📦 What You Downloaded

You have TWO solutions to choose from:

1. **Python Script** - For quick, internal processing
2. **Web Application** - For client-facing, professional interface

---

## ⚡ Quick Start (Choose Your Path)

### Path A: Just Want to Process Data Now? (5 minutes)

1. **Download:** `competency_data_merge_flexible.py`

2. **Install pandas:**
   ```bash
   pip install pandas
   ```

3. **Prepare your files:**
   - Name them: `csv1_raw_data.csv` and `csv2_desired_state_mapping.csv`
   - Put them in same folder as the script

4. **Run:**
   ```bash
   python competency_data_merge_flexible.py
   ```

5. **Done!** Get your output: `csv1_updated.csv`

---

### Path B: Want to Give Client a Web Tool? (15 minutes)

1. **Download & Extract:** `webapp_package.zip`

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test locally:**
   ```bash
   python app.py
   ```
   Open: http://localhost:5000

4. **Deploy online** (Choose one):
   
   **Option 1: PythonAnywhere (Easiest!)**
   - Go to: https://www.pythonanywhere.com
   - Create free account
   - Upload your files
   - Follow their Flask setup wizard
   - Share link with client!
   
   **Option 2: Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```
   
   **Option 3: Render**
   - Connect GitHub
   - Click "Deploy"
   - Done!

---

## 📋 What Each File Does

### Python Script Package
```
competency_data_merge_flexible.py
└── The main processing script (works with any questionnaire!)
```

### Web App Package
```
webapp_package.zip
├── app.py                  # Main Flask application
├── templates/
│   └── index.html         # Web interface
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── runtime.txt           # Python version
├── .gitignore            # Git ignore rules
├── README_WEBAPP.md      # Web app documentation
└── DEPLOYMENT_GUIDE.md   # Deployment instructions
```

---

## 🎯 Key Features (Both Solutions)

### ✅ Automatic Question Detection
- Works with Q1-Q27, Q1-Q30, Q1-Q25, or any number!
- No code changes needed
- Detects questions automatically

### ✅ Multi-Department Support
- Sales
- Application Engineering
- Commercial Operations
- Add more anytime!

### ✅ Smart Processing
- Only updates "Desired State" rows
- Validates all columns
- Detailed error messages
- Shows progress

---

## 📊 How It Works

```
┌─────────────────┐
│   CSV 1         │  ← Your raw assessment data
│   (Raw Data)    │     - Has "Raters Group" column
│                 │     - Has "Desired_State" column
└────────┬────────┘     - Has Q1, Q2, Q3... columns
         │
         │ Find rows where
         │ Raters Group = "Desired State"
         │
         ▼
┌─────────────────┐
│   CSV 2         │  ← Your reference data
│   (Desired      │     - Has "Desired State" column
│    State Map)   │     - Has Q1, Q2, Q3... columns
└────────┬────────┘
         │
         │ Look up matching
         │ Desired State value
         │
         ▼
┌─────────────────┐
│   Output        │  ← Merged result
│   (Updated CSV) │     - Original data
│                 │     + Desired State questions filled
└─────────────────┘
```

---

## 🔍 File Requirements

### CSV 1 (Raw Data) MUST have:
- Column: `Raters Group`
- Column: `Desired_State`
- Columns: `Q1_Something_Something`, `Q2_...`, etc.

### CSV 2 (Desired State Mapping) MUST have:
- Column: `Desired State`
- Columns: Same Q1, Q2, Q3... as CSV 1

### 💡 Important Notes:
- Column names must match EXACTLY (including spaces)
- "Desired State" in CSV 2 = "Desired_State" values in CSV 1
- Questions auto-detected (starts with Q + number)

---

## 🛠️ Troubleshooting

### "Module not found"
```bash
pip install pandas
# or for web app:
pip install -r requirements.txt
```

### "Column not found"
- Check spelling of column names
- Check for extra spaces
- Column names are case-sensitive

### "No matching rows"
- Verify CSV 1 has rows where "Raters Group" = "Desired State"
- Check the exact text (case-sensitive)

### "No match found in CSV 2"
- Check "Desired State" values exist in CSV 2
- Values must match exactly

### Web app won't start
```bash
# Try different port
# Edit app.py, change last line to:
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

## 📚 Documentation Files

- **WHICH_SOLUTION.md** - Help choosing between script vs web app
- **DEPLOYMENT_GUIDE.md** - Detailed deployment instructions
- **README_WEBAPP.md** - Web app technical details

---

## 💻 Example Usage

### Python Script
```bash
# Using default file names
python competency_data_merge_flexible.py

# Using custom file names
python competency_data_merge_flexible.py sales_raw.csv sales_desired.csv sales_output.csv

# Works with any department's questionnaire!
python competency_data_merge_flexible.py appeng_raw.csv appeng_desired.csv appeng_output.csv
```

### Web App
```
1. Visit: http://localhost:5000 (or your deployed URL)
2. Select: "Sales" (or other department)
3. Upload: Raw data CSV
4. Upload: Desired state CSV
5. Click: "Process & Download"
6. Get: Merged file downloaded automatically!
```

---

## 🎉 Success Checklist

For Python Script:
- [ ] Python installed
- [ ] Pandas installed
- [ ] CSV files prepared
- [ ] Script runs successfully
- [ ] Output file created

For Web App:
- [ ] Dependencies installed
- [ ] App runs locally (http://localhost:5000)
- [ ] Can upload files
- [ ] Can download results
- [ ] (Optional) Deployed online
- [ ] (Optional) Shared with client

---

## 🆘 Still Need Help?

1. **Check error messages** - They're detailed and point to the issue
2. **Verify CSV files** - Correct columns, correct values
3. **Test with small sample** - Use 5-10 rows first
4. **Read the guides** - DEPLOYMENT_GUIDE.md has answers

---

## 🎊 You're All Set!

Choose your path:
- **Quick processing?** → Use Python script
- **Client tool?** → Deploy web app

Both work with all departments automatically! 🚀

Happy processing! 🎯
