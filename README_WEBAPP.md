# Competency Assessment Data Merge Tool 🎯

A web application for merging competency assessment data with desired state mappings across different departments.

## Features

✨ **Department Support**
- Sales
- Application Engineering  
- Commercial Operations

🔄 **Automatic Processing**
- Detects question columns automatically (Q1, Q2, Q3...)
- Works with any number of questions
- No code changes needed for different questionnaires

📊 **User-Friendly Interface**
- Simple dropdown selection
- Drag-and-drop file upload
- Instant download of processed results

## Quick Start

### Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

3. Open browser:
```
http://localhost:5000
```

### Usage

1. Select your department from the dropdown
2. Upload your raw data CSV file
3. Upload your desired state mapping CSV file
4. Click "Process & Download"
5. Get your merged data file!

## File Requirements

### CSV 1 (Raw Data) must include:
- `Raters Group` column
- `Desired_State` column
- Question columns (Q1_..., Q2_..., etc.)

### CSV 2 (Desired State Mapping) must include:
- `Desired State` column (matches values in CSV 1's `Desired_State`)
- Same question columns as CSV 1

## How It Works

The tool:
1. Identifies rows where `Raters Group` = "Desired State"
2. Looks up the `Desired_State` value
3. Finds matching row in CSV 2
4. Copies all Q1-Q27 (or more) values from CSV 2 to CSV 1
5. Returns the merged file

## Deployment

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions to:
- Heroku
- PythonAnywhere
- Render

## Tech Stack

- **Backend:** Flask (Python)
- **Data Processing:** Pandas
- **Frontend:** HTML5, CSS3, JavaScript

## Security

Before production deployment:
1. Change the secret key in `app.py`
2. Set up proper environment variables
3. Configure HTTPS

## Support

For issues or questions, check:
1. Error messages in the web interface
2. Console logs for detailed debugging
3. Verify CSV files have correct column names

## License

Proprietary - Internal Use Only
