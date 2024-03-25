import { useState, useEffect, useMemo } from "react";
import "./styles.css";
import { CAR_LIST, PRICE_LIST } from "./cars";
/**
 * 1. Create a clock show current time
 *    Format: HH:mm:ss
 *
 * 2. Render Car List
 *  e.g.
 *    - Honda Vezel - New - $2000
 *    - Honda Civic - Used - $3000
 *
 * 3. Create a search box, search cars by make & model
 *  e.g
 *    - search Honda - the list renders 2 cars
 *    - search Vezel - the list renders 1 car
 *    - search A3 Vezel - the list renders 2 cars
 */

export default function App() {
  const [time, setTime] = useState("00:00:00");
  const [cars, setCars] = useState(CAR_LIST);

  const priceMapping = useMemo(() => {
    const mapping = {};
    PRICE_LIST.forEach((price) => {
        mapping[price.car_id] = price.price;
    });
    return mapping;
  }, [PRICE_LIST]);

  useEffect(() => {
    setTimeout(() => {
      const id = setTime(getCurrentTime());
      return () => clearTimeout(id);
    }, 1000);
  }, [time]);

  const getCurrentTime = () => {
    const date = new Date();
    const hours = date
      .getHours()
      .toLocaleString("en", { minimumIntegerDigits: 2 });
    const minutes = date
      .getMinutes()
      .toLocaleString("en", { minimumIntegerDigits: 2 });
    const seconds = date
      .getSeconds()
      .toLocaleString("en", { minimumIntegerDigits: 2 });
    return `${hours}:${minutes}:${seconds}`;
  };

  const carList = () => {
    return (
      <ul>
        {cars.map((car) => (
          <li key={`${car.id}${car.model}`}>
            {car.make} - {car.model} - {car.type} - ${priceMapping[car.id]}
          </li>
        ))}
      </ul>
    );
  };

  const [searchText, setSearchText] = useState();

  // honda vezel
  const handleSearchChange = (e) => {
    const targetValue = e.target.value;
    setSearchText(targetValue);

    if (targetValue.length === 0) {
      return setCars(CAR_LIST);
    }

    const valueArray = targetValue.toLowerCase().split(" ");

    const filteredCars = CAR_LIST.filter((car) => {
      return valueArray.some((word) =>
        `${car.make}${car.model}`.toLowerCase().includes(word)
      );
    });

    setCars(filteredCars);
  };

  const searchBox = () => {
    return <input value={searchText} onChange={handleSearchChange}></input>;
  };
  const clock = () => <h2>{time}</h2>;
  return (
    <div className="App">
      {clock()}
      {searchBox()}
      {carList()}
      <h2>Start editing to see some magic happen!</h2>
    </div>
  );
}
