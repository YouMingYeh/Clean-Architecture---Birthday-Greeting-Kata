const BASE_URL = 'http://localhost:5000';

export const sendGreetingsV1 = async (format: string, db: string, date: string) => {
    const parsedDate = date.split('/').join('-');
    const response = await fetch(`${BASE_URL}/greetings/v1?format=${format}&db=${db}&date=${parsedDate}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });

    return response.json();
}

export const sendGreetingsV2 = async (format: string, db: string, date: string) => {
    const parsedDate = date.split('/').join('-');
    const response = await fetch(`${BASE_URL}/greetings/v2?format=${format}&db=${db}&date=${parsedDate}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    return response.json();
}

export const sendGreetingsV3 = async (format: string, db: string, date: string, picture_path: string) => {
    const parsedDate = date.split('/').join('-');
    const response = await fetch(`${BASE_URL}/greetings/v3?format=${format}&db=${db}&date=${parsedDate}&picture_path=${picture_path}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    return response.json();
}

export const sendGreetingsV4 = async (format: string, db: string, date: string, discount_for_male: number, items_for_male: string[], discount_for_female: number, items_for_female: string[]) => {
    const parsedDate = date.split('/').join('-');
    const maleItemsQueryParam = items_for_male.map(item => `items_for_male=${encodeURIComponent(item)}`).join('&');
    const femaleItemsQueryParam = items_for_female.map(item => `items_for_female=${encodeURIComponent(item)}`).join('&');
    const response = await fetch(`${BASE_URL}/greetings/v4?format=${format}&db=${db}&date=${parsedDate}&discount_for_male=${discount_for_male}&discount_for_female=${discount_for_female}&${maleItemsQueryParam}&${femaleItemsQueryParam}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    return response.json();
}


// Function to parse JSON response
function parseJsonResponse(response: any[]): any[] {
    return response.map(item => JSON.parse(item));
  }
  
  // Function to parse XML response
  function parseXmlResponse(response: any[]): Document[] {
    const parser = new DOMParser();
    return response.map(item => parser.parseFromString(item, "application/xml"));
  }
  