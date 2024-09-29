# Email Attachment Extractor from MBOX Files

This project provides a Python script to extract attachments from an MBOX file and save them to a specified folder. It processes each email in the MBOX file, reads its date and subject, and saves attachments with filenames based on the date of the email and the original attachment name. This can be particularly useful for organizing and managing email data for archival or analysis purposes.

## Features

- Extracts attachments from emails stored in an MBOX file.
- Saves the attachments in a specified folder.
- Filenames are formatted with the email date and cleaned to avoid any file system conflicts.

## Prerequisites

- Python 3.x
- The following Python libraries:
  - `mailbox`
  - `os`
  - `dateutil` (install with `pip install python-dateutil`)
  - `email`
  - `re`

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/devaftab/Attachment_Harvester.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Attachment_Harvester
   ```
3. Install required dependencies:
   ```bash
   pip install python-dateutil
   ```

### Usage

1. Place the MBOX file in a desired directory or specify the path to the MBOX file.

2. Open the `extract_attachments.py` file and update the following variables:

   ```python
   mbox_file = '<mbox file path>'
   output_folder = '<output_folder_path>'
   ```

   Replace `<mbox file path>` with the path to your MBOX file and `<output_folder_path>` with the path where attachments should be saved.

3. Run the script:
   ```bash
   python extract_attachments.py
   ```
   The attachments will be saved to the specified folder.

### Code Explanation

The script includes the following main components:

- **`extract_attachments_from_mbox(mbox_file, output_folder)`:** This function reads the MBOX file and extracts attachments from each email. The extracted files are saved in the specified folder, and the filenames are prefixed with the email's date.
- **`clean_filename(filename)`:** A utility function to clean up filenames, removing any invalid characters or whitespaces.

- **`decode_header` from the `email.header` module:** Decodes the subject and filenames in case they are encoded in non-ASCII formats.

### Example Output

If the email date is `2023-09-15` and the attachment is named `report.pdf`, the saved file will have the following format:

```
2023-09-15_report.pdf
```

### Limitations

- Only single-part attachments are currently handled.
- If two attachments have the same name and date, they will be overwritten. Consider modifying the script to add unique identifiers in such cases.

### Contribution

Feel free to submit issues or pull requests if you have any suggestions or improvements.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
