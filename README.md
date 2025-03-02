# Job Search Tool

## Description

This Python application helps users find job opportunities using the Google Jobs API through SerpAPI. The tool allows searching for jobs based on job title and location, with results exportable to CSV format for further analysis.

## Features

- Search jobs by title and location
- Accumulate multiple search results
- Export job listings to CSV file
- User-friendly command line interface
- Detailed job information including title, company, location, and description

## Requirements

- Python 3.6+
- requests
- pandas

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/job-search-tool.git

# Navigate to the project directory
cd job-search-tool

# Install dependencies
pip install requests pandas
```

## Configuration

You need to obtain a SerpAPI key and replace it in the script:

```python
API_KEY = "YOUR_SERPAPI_KEY"
```

Get your API key by registering at [SerpAPI](https://serpapi.com/).

## Usage

Run the script and follow the interactive prompts:

```bash
python jobSearch.py
```

The application will guide you through:
1. Entering job titles to search for
2. Specifying location preferences
3. Saving results to CSV or continuing with more searches

## Output

The tool generates a CSV file named `empleos_resultados.csv` with the following information:
- Job title
- Company name
- Location
- Source (where the job was posted)
- Description
- Application link

## Limitations

- Requires a valid SerpAPI key (free tier has limited searches)
- Results are limited to what Google Jobs API provides
- English and Spanish language support only

## License

This project is licensed under the MIT License - see the LICENSE file for details.
