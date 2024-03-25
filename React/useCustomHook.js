import {useState, useEffect} from 'react';

export default useCustomHook = (url) => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const fetchData = async() => {
        try {
            const response = await fetch(url);
            const jsonData = await response.json();
            if (!response.ok) {
                throw Error("error");
            }
            setData(jsonData);
        } catch (error) {
            setError(error);
            console.log(error);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        fetchData();
    }, [url]);


    return {data, loading, error};
};