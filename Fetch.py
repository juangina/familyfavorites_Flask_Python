import requests

getTopics = {


    #promise version of getImages
    getImages(imageTopic) {
        return fetch(
            "https://api.pexels.com/v1/search?query=" + imageTopic + "&per_page=1",
            {
                method: "GET",
                headers: {
                    "Authorization": "563492ad6f91700001000001e0f967773c3c4b39bac3b35ac6b5496f",
                },
                maxRedirects: 20
            })
            .then(response => {
                return response.json();
            })
            .then(jsonResponse => {
                if(jsonResponse) {
                    return jsonResponse;
                }
            })
    },

    #promise version of get Image
    getImage(imageIndex, imageTopic) {
        return fetch(
            "https://api.pexels.com/v1/search?page=" + imageIndex + "&query=" + imageTopic + "&per_page=1",
            {
                method: "GET",
                headers: {
                    "Authorization": "563492ad6f91700001000001e0f967773c3c4b39bac3b35ac6b5496f",
                },
                maxRedirects: 20
            })
            .then(response => {
                return response.json();
            })
            .then(jsonResponse => {
                if(jsonResponse) {
                    return jsonResponse;
                }
            })
    },

    #promise version of get Quote
    getQuote() {
        return fetch(
            "https://cors-anywhere.herokuapp.com/https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&jsonp=?"
           )
            .then(response => {
                return response.json();
            })
            .then(jsonResponse => {
                if(jsonResponse) {
                    return jsonResponse;
                }
            })
    }
}

