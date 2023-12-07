"use client";
import Select from "./components/Select";
import DateSelect from "./components/DateSelect";
import TextInputField from "./components/TextInputField";
import DiscountItemsInput from "./components/DiscountItems";
import Button from "./components/Button";
import {
  sendGreetingsV1,
  sendGreetingsV2,
  sendGreetingsV3,
  sendGreetingsV4,
} from "./APIs";
import { useState, useEffect } from "react";
import xml2js from "xml2js";

/**
 * Renders the Home component.
 * @returns The rendered Home component.
 */

export default function Home() {
  const [versions, setVersions] = useState<string[]>([
    "Version 1: Simple Message",
    "Version 2: Simple Message with full name",
    "Version 3: Message with an Elder Picture for those whose age is over 49.",
    "Version 4: Tailer-made Message for different gender",
  ]);
  const [selectedVersion, setSelectedVersion] = useState<string>("");
  const [date, setDate] = useState<Date | null>(null);
  const [formats, setFormats] = useState<string[]>(["JSON", "XML"]);
  const [selectedFormat, setSelectedFormat] = useState<string>("");
  const [dbs, setDbs] = useState<string[]>(["memory", "mongo", "mysql"]);
  const [selectedDb, setSelectedDb] = useState<string>("");
  const [picture_path, setPicturePath] = useState<string>("");
  const [discount_for_female, setDiscountForFemale] = useState<number>(0);
  const [discount_for_male, setDiscountForMale] = useState<number>(0);
  const [items_for_female, setItemsForFemale] = useState<string[]>([]);
  const [items_for_male, setItemsForMale] = useState<string[]>([]);
  const [response, setResponse] = useState<any[]>();
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const onVersionChange = (value: string) => {
    value = value.substring(0, 9);
    setResponse([]);
    setSelectedVersion(value);
  };

  const onFormatChange = (value: string) => {
    setResponse([]);
    setSelectedFormat(value);
  };

  const onDbChange = (value: string) => {
    setResponse([]);
    setSelectedDb(value);
  };

  const onPicturePathChange = (value: string) => {
    setResponse([]);
    setPicturePath(value);
  };

  const onGreet = () => {
    setResponse([]);
    if (date === null) {
      alert("Please select a date!");
      return;
    }
    if (selectedFormat === "") {
      alert("Please select a format!");
      return;
    }
    if (selectedVersion === "") {
      alert("Please select a version!");
      return;
    }
    setIsLoading(true);
    switch (selectedVersion) {
      case "Version 1":
        sendGreetingsV1(
          selectedFormat,
          selectedDb,
          date?.toLocaleDateString("fr-CA")
        )
          .then((res) => {
            setResponse(res);
          })
          .finally(() => {
            setIsLoading(false);
          });
        break;
      case "Version 2":
        sendGreetingsV2(
          selectedFormat,
          selectedDb,
          date?.toLocaleDateString("fr-CA")
        )
          .then((res) => {
            setResponse(res);
          })
          .finally(() => {
            setIsLoading(false);
          });
        break;
      case "Version 3":
        sendGreetingsV3(
          selectedFormat,
          selectedDb,
          date?.toLocaleDateString("fr-CA"),
          picture_path
        )
          .then((res) => {
            setResponse(res);
          })
          .finally(() => {
            setIsLoading(false);
          });
        break;
      case "Version 4":
        sendGreetingsV4(
          selectedFormat,
          selectedDb,
          date?.toLocaleDateString("fr-CA"),
          discount_for_male,
          items_for_male,
          discount_for_female,
          items_for_female
        )
          .then((res) => {
            setResponse(res);
          })
          .finally(() => {
            setIsLoading(false);
          });
        break;
    }
  };

  useEffect(() => {
    console.log(response);
    if (isLoading) {
      // Show loading effect
    } else {
      // Hide loading effect
    }
  }, [isLoading]);

  return (
    <main className="py-8 sm:px-12 md:px-24 lg:px-64 xl:px-96">
      <h1 className="text-4xl font-bold mb-4 text-center ">
        Birthday Greeting Kata
      </h1>
      <h2 className="text-2xl mb-4 text-center">
        Clean Architecture Birthday Greeting Kata
      </h2>
      <div className="flex flex-col space-y-4">
        <div className="flex flex-col items-start">
          <h3>Select an API Version:</h3>
          <Select
            options={versions}
            onChange={onVersionChange}
            placeholder={"Default Version"}
          ></Select>
        </div>

        <div className="flex flex-col items-start">
          <h3>Select a Date of Birth:</h3>
          <DateSelect onDateChange={setDate}></DateSelect>
        </div>
        <div className="flex flex-col items-start">
          <h3>Select a Format:</h3>
          <Select
            options={formats}
            onChange={onFormatChange}
            placeholder={"Default Format"}
          ></Select>
        </div>

        <div className="flex flex-col items-start">
          <h3>Select a Database:</h3>
          <Select
            options={dbs}
            onChange={onDbChange}
            placeholder={"Default Database"}
          ></Select>
        </div>

        {selectedVersion === "Version 3" && (
          <div className="flex flex-col items-start">
            <h3>Enter a Picture Url:</h3>
            <TextInputField
              value={picture_path}
              onChange={onPicturePathChange}
              placeholder="a Picture Url"
            ></TextInputField>
          </div>
        )}
        {selectedVersion === "Version 4" && (
          <div className="flex flex-col items-start">
            <h3>Enter discount and items for female:</h3>
            <DiscountItemsInput
              initialDiscount={discount_for_female}
              initialItems={items_for_female}
              onDiscountChange={setDiscountForFemale}
              onItemsChange={setItemsForFemale}
            ></DiscountItemsInput>
          </div>
        )}
        {selectedVersion === "Version 4" && (
          <div className="flex flex-col items-start">
            <h3>Enter discount and items for male:</h3>
            <DiscountItemsInput
              initialDiscount={discount_for_male}
              initialItems={items_for_male}
              onDiscountChange={setDiscountForMale}
              onItemsChange={setItemsForMale}
            ></DiscountItemsInput>
          </div>
        )}
      </div>
      <div className="flex flex-col items-center min-w-full">
        <Button label={"Greet!"} onClick={onGreet}></Button>
      </div>
      <div className="flex flex-col mt-4 items-start ">
        <h2>Response:</h2>
        {isLoading ? (
          <p>Loading...</p>
        ) : (
          <>
            <div>{response?.map((e) => e)}</div>
            <h2>Parsed:</h2>
            <div>{response && parseResponse(response, selectedFormat)}</div>
          </>
        )}
      </div>
    </main>
  );
}
const parseResponse = (response: any[], format: string): any[] => {
  switch (format) {
    case "JSON":
      return parseJsonResponse(response);
    case "XML":
      return parseXmlResponse(response);
    default:
      return [];
  }
};
const parseJsonResponse = (response: any[]): any[] => {
  return response?.map((item) => {
    const parsedItem = JSON.parse(item);
    return (
      <div className="bg-gray-200 p-4 rounded-md mt-4">
        <pre className="text-gray-800">
          <p>Title: {parsedItem.title}</p>
          <p>Content: {parsedItem.content}</p>
          {parsedItem.picture_path && <img src={parsedItem.picture_path}></img>}
        </pre>
      </div>
    );
  });
};

const parseXmlResponse = (responses: any[]): JSX.Element[] => {
  const result: JSX.Element[] = [];

  responses.forEach((xmlString, index) => {
    try {
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(xmlString, "application/xml");

      // Extract data from xmlDoc and create HTML elements
      const title =
        xmlDoc.querySelector("title")?.textContent || `No Title ${index + 1}`;
      const content =
        xmlDoc.querySelector("content")?.textContent ||
        `No Content ${index + 1}`;
      const picture =
        xmlDoc.querySelector("picture_path")?.textContent ||
        `No Picture ${index + 1}`;

      const titleElement = (
        <div key={index} className="bg-gray-200 p-4 rounded-md mt-4">
          <p className="text-gray-800">Title: {title}</p>
        </div>
      );

      const contentElement = (
        <div key={index} className="bg-gray-200 p-4 rounded-md mt-4">
          <p className="text-gray-800">Content: {content}</p>
        </div>
      );

      const pictureElement =
        picture !== `No Picture ${index + 1}` && (
          <div key={index} className="bg-gray-200 p-4 rounded-md mt-4">
            <img src={picture} alt="No Picture" />
          </div>
        );

      result.push(titleElement);
      result.push(contentElement);
      if (pictureElement) result.push(pictureElement);
    } catch (error) {
      console.error(`Error parsing XML at index ${index}:`, error);
    }
  });

  return result;
};
