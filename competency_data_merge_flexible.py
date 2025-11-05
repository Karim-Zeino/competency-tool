import pandas as pd
import sys

def merge_competency_data(csv1_path, csv2_path, output_path='output_updated.csv'):
    """
    Merges competency assessment data from two CSV files.
    Automatically detects question columns (Q1-Q27, Q1-Q30, etc.) without hardcoding.
    
    Args:
        csv1_path: Path to raw data CSV file
        csv2_path: Path to desired state mapping CSV file
        output_path: Path for output file (default: output_updated.csv)
    """
    
    # Load the CSV files
    print("Loading CSV files...")
    try:
        csv1 = pd.read_csv(csv1_path)
        csv2 = pd.read_csv(csv2_path)
    except FileNotFoundError as e:
        print(f"ERROR: Could not find file - {e}")
        return False
    except Exception as e:
        print(f"ERROR: Failed to load CSV files - {e}")
        return False
    
    print(f"✓ CSV 1 loaded: {len(csv1)} rows, {len(csv1.columns)} columns")
    print(f"✓ CSV 2 loaded: {len(csv2)} rows, {len(csv2.columns)} columns")
    
    # Automatically detect question columns (columns starting with Q and a number)
    question_columns = [col for col in csv1.columns if col.startswith('Q') and '_' in col]
    
    # Filter to only include questions that exist in both CSV files
    question_columns = [col for col in question_columns if col in csv2.columns]
    
    print(f"\n✓ Detected {len(question_columns)} question columns to merge")
    print(f"  First few: {question_columns[:3]}")
    print(f"  Last few: {question_columns[-3:]}")
    
    # Verify required columns exist
    if 'Raters Group' not in csv1.columns:
        print("ERROR: 'Raters Group' column not found in CSV 1")
        return False
    
    if 'Desired_State' not in csv1.columns:
        print("ERROR: 'Desired_State' column not found in CSV 1")
        return False
    
    if 'Desired State' not in csv2.columns:
        print("ERROR: 'Desired State' column not found in CSV 2")
        return False
    
    # Find rows in CSV1 where Raters Group = "Desired State"
    desired_state_mask = csv1['Raters Group'] == 'Desired State'
    rows_to_update = csv1[desired_state_mask].copy()
    
    print(f"\n✓ Found {len(rows_to_update)} rows with 'Raters Group' = 'Desired State'")
    
    if len(rows_to_update) == 0:
        print("WARNING: No rows found to update. Check that 'Raters Group' column contains 'Desired State' values.")
        csv1.to_csv(output_path, index=False)
        print(f"\nOriginal data saved to: {output_path}")
        return True
    
    # Counter for tracking updates
    updates_made = 0
    no_match_count = 0
    no_match_list = []
    
    print("\nProcessing updates...")
    print("-" * 60)
    
    # Iterate through each row that needs updating
    for idx in csv1[desired_state_mask].index:
        # Get the Desired_State value for this row
        desired_state_value = csv1.loc[idx, 'Desired_State']
        
        # Find the matching row in CSV2
        matching_rows = csv2[csv2['Desired State'] == desired_state_value]
        
        if len(matching_rows) > 0:
            # Get the first matching row (assuming unique Desired State values in CSV2)
            match = matching_rows.iloc[0]
            
            # Update each question column in CSV1 with values from CSV2
            for col in question_columns:
                csv1.loc[idx, col] = match[col]
            
            updates_made += 1
            print(f"✓ Updated row {idx} - Desired State: '{desired_state_value}'")
        else:
            no_match_count += 1
            no_match_list.append(desired_state_value)
            print(f"✗ No match found in CSV2 for Desired State: '{desired_state_value}' (row {idx})")
    
    # Save the updated CSV1
    csv1.to_csv(output_path, index=False)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"SUMMARY:")
    print(f"{'='*60}")
    print(f"Total rows to process: {len(rows_to_update)}")
    print(f"Successfully updated: {updates_made}")
    print(f"No match found: {no_match_count}")
    
    if no_match_count > 0:
        print(f"\nDesired State values with no match:")
        for val in set(no_match_list):
            print(f"  - '{val}'")
    
    print(f"\n✓ Output saved to: {output_path}")
    print(f"{'='*60}")
    
    return True


if __name__ == "__main__":
    # Check if filenames are provided as command line arguments
    if len(sys.argv) >= 3:
        csv1_file = sys.argv[1]
        csv2_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) >= 4 else 'output_updated.csv'
    else:
        # Use default filenames
        csv1_file = 'csv1_raw_data.csv'
        csv2_file = 'csv2_desired_state_mapping.csv'
        output_file = 'csv1_updated.csv'
    
    print("="*60)
    print("COMPETENCY ASSESSMENT DATA MERGE TOOL")
    print("="*60)
    print(f"Input file 1 (raw data): {csv1_file}")
    print(f"Input file 2 (desired state mapping): {csv2_file}")
    print(f"Output file: {output_file}")
    print("="*60)
    print()
    
    success = merge_competency_data(csv1_file, csv2_file, output_file)
    
    if success:
        print("\n✓ Process completed successfully!")
    else:
        print("\n✗ Process failed. Please check the errors above.")
        sys.exit(1)
