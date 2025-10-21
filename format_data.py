import pandas as pd
import os
import sys


class LicenseDataFormatter:
    def __init__(
        self,
        input_file: str = "licenses/main.txt",
        output_file: str = "licenses/main.csv",
    ):
        self.input_file = input_file
        self.output_file = output_file

    def _validate_input_file(self) -> bool:
        if not os.path.exists(self.input_file):
            print(f"❌ Error: Input file '{self.input_file}' not found.")
            return False

        if not os.path.isfile(self.input_file):
            print(f"❌ Error: '{self.input_file}' is not a file.")
            return False

        return True

    def _read_tab_separated_data(self) -> pd.DataFrame:
        try:
            # Read the tab-separated file
            df = pd.read_csv(self.input_file, sep="\t", encoding="utf-8")

            # Clean column names (remove extra spaces)
            df.columns = df.columns.str.strip()

            # Rename columns to match expected format
            column_mapping = {"Licencias ESET": "Licencias", "Licencias": "Licencias"}

            df = df.rename(columns=column_mapping)

            # Add the new 'estatus' column with default value
            df["Estatus"] = "Pendiente"

            return df

        except Exception as e:
            print(f"❌ Error reading file: {str(e)}")
            return None

    def _validate_data(self, df: pd.DataFrame) -> bool:
        """
        Validate the data structure and content.

        Args:
            df (pd.DataFrame): DataFrame to validate

        Returns:
            bool: True if data is valid, False otherwise
        """
        required_columns = ["Producto", "Licencias", "Vencimiento", "Tipo", "Estatus"]

        # Check if all required columns exist
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"❌ Missing required columns: {missing_columns}")
            return False

        # Check for empty data
        if df.empty:
            print("❌ No data found in the file.")
            return False

        # Check for missing license keys
        empty_licenses = df["Licencias"].isna().sum()
        if empty_licenses > 0:
            print(f"⚠️  Warning: {empty_licenses} empty license entries found.")

        return True

    def _save_to_csv(self, df: pd.DataFrame) -> bool:
        """
        Save the DataFrame to CSV format.

        Args:
            df (pd.DataFrame): DataFrame to save

        Returns:
            bool: True if saved successfully, False otherwise
        """
        try:
            # Create output directory if it doesn't exist
            output_dir = os.path.dirname(self.output_file)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                print(f"📁 Created directory: {output_dir}")

            # Save to CSV
            df.to_csv(self.output_file, index=False, encoding="utf-8")

            return True

        except Exception as e:
            print(f"❌ Error saving file: {str(e)}")
            return False

    def _display_summary(self, df: pd.DataFrame) -> None:
        """
        Display a summary of the processed data.

        Args:
            df (pd.DataFrame): DataFrame to summarize
        """
        print("\n" + "=" * 50)
        print("📊 DATA SUMMARY")
        print("=" * 50)
        print(f"Total records: {len(df)}")
        print(f"Products: {df['Producto'].value_counts().to_dict()}")
        print(f"License types: {df['Tipo'].value_counts().to_dict()}")
        print(f"Expiration dates: {df['Vencimiento'].value_counts().to_dict()}")
        print(f"Status: {df['Estatus'].value_counts().to_dict()}")

        # Show first few records
        print("\n🔍 Sample data:")
        print(df.head().to_string(index=False))

    def format_data(self) -> bool:
        """
        Main method to format the data from text to CSV.

        Returns:
            bool: True if formatting was successful, False otherwise
        """
        print("🚀 Starting license data formatting...")
        print(f"📂 Input file: {self.input_file}")
        print(f"📄 Output file: {self.output_file}")

        # Validate input file
        if not self._validate_input_file():
            return False

        # Read data
        df = self._read_tab_separated_data()
        if df is None:
            return False

        # Validate data
        if not self._validate_data(df):
            return False

        # Save to CSV
        if not self._save_to_csv(df):
            return False

        # Display summary
        self._display_summary(df)

        print("\n✅ Data formatting completed successfully!")
        return True


def main():
    """Main function to run the data formatter."""
    try:
        # Default file paths
        input_file = "licenses/main.txt"
        output_file = "licenses/main.csv"

        # Allow command line arguments
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
        if len(sys.argv) > 2:
            output_file = sys.argv[2]

        # Create formatter instance and run
        formatter = LicenseDataFormatter(input_file, output_file)
        success = formatter.format_data()

        if success:
            print(f"\n🎉 Done! CSV file created at: {output_file}")
            sys.exit(0)
        else:
            print("\n❌ Formatting failed!")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
