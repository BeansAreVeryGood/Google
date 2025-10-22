# Google Search Site

This project is a simple web application that allows users to perform Google searches directly from the site. The search results will open in a new tab, keeping the user on the original site.

## Project Structure

```
google-search-site
├── public
│   ├── index.html        # Main HTML document for the website
│   ├── search.html       # Secondary HTML document for displaying search results
│   ├── css
│   │   └── styles.css    # Styles for the website
│   └── js
│       └── search.js     # JavaScript logic for handling search functionality
├── src
│   └── components
│       └── search-tab.js  # Component for the search tab
├── .gitignore            # Files and directories to be ignored by Git
├── package.json          # Configuration file for npm
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd google-search-site
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   Open `public/index.html` in your web browser to view the site.

## Usage

- Enter your search query in the search tab and click the search button.
- The search results will open in a new tab, allowing you to view them without leaving the site.

## Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.