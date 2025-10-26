import streamlit as st
import requests
import datetime

API_KEY = "61c465d2171b77b3cc7c0d5f578ca7ab"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"

def get_new_movies():
    today = datetime.date.today()
    thirty_days_ago = today - datetime.timedelta(days=30)
    
    params = {
        "api_key": API_KEY,
        "sort_by": "release_date.desc",
        "primary_release_date.gte": thirty_days_ago,
        "primary_release_date.lte": today,
        "language": "en-US",
        "page": 1
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()  # Fixed: was response.get().json()
        return data  # Fixed: was missing return statement
    except requests.exceptions.RequestException as e:
        st.error(f"API request failed: {str(e)}")
        return None
    except ValueError as e:
        st.error(f"Invalid JSON response: {str(e)}")
        return None

st.title("New Movies Released in the Last 30 Days")

if st.button("Find New Movies", key="find_movies"):
    data = get_new_movies()
    
    if data is None:  # Fixed: Check if data is None first
        st.error("Failed to fetch movie data")
    else:
        results = data.get('results', [])
        
        if not results:
            st.write("No new movies found.")
        else:
            st.success(f"Found {len(results)} new movies!")
            for movie in results:
                st.subheader(movie.get('title', 'Unknown Title'))
                st.caption(f"Release Date: {movie.get('release_date', 'N/A')}")
                
                # Show rating if available
                rating = movie.get('vote_average')
                if rating:
                    st.caption(f"⭐ Rating: {rating}/10")
                
                overview = movie.get('overview', 'No description available.')
                st.write(overview)
                st.divider()