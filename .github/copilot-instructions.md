# AI Agent Instructions for Movie Discovery App

## Project Overview
This is a Streamlit-based web application that displays recently released movies using The Movie Database (TMDB) API. The app provides a simple interface to view movies released in the last 30 days.

## Key Components

### API Integration
- TMDB API is used for movie data (`BASE_URL = "https://api.themoviedb.org/3/discover/movie"`)
- API key is stored directly in the code (Note: Consider moving to environment variables)
- Queries are constructed using the `requests` library

### User Interface
- Built with Streamlit for interactive web components
- Main interface components defined in `tester.py`:
  - Title banner
  - "Find New Movies" button
  - Movie cards showing title, release date, and overview

### Data Processing
- Date handling uses Python's `datetime` module
- Movie data is filtered for the last 30 days
- Results are processed using dictionary get() method with fallbacks

## Development Setup
1. Install required dependencies:
   ```
   pip install streamlit requests
   ```
2. Run the application:
   ```
   streamlit run tester.py
   ```

## Project Conventions
- Error handling uses defensive programming with `.get()` and default values
- Date calculations are done using `datetime.timedelta`
- UI components follow Streamlit's hierarchical structure (title → subheader → caption → content)

## Integration Points
- TMDB API: Used for movie discovery with following parameters:
  - `sort_by`: Release date descending
  - `primary_release_date`: Date range filter
  - `language`: English (en-US)
  - `page`: Pagination support

## Areas for Improvement
- API key should be moved to environment variables
- Error handling for API requests should be implemented
- Pagination support could be added for viewing more results
- Movie poster images could be added to enhance visual appeal