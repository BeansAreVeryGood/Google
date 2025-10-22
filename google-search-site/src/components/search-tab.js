import React, { useState } from 'react';

const SearchTab = () => {
    const [query, setQuery] = useState('');

    const handleSearch = (event) => {
        event.preventDefault();
        if (query) {
            const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
            window.open(searchUrl, '_blank');
        }
    };

    return (
        <div className="search-tab">
            <form onSubmit={handleSearch}>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search Google..."
                    required
                />
                <button type="submit">Search</button>
            </form>
        </div>
    );
};

export default SearchTab;