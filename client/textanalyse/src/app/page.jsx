"use client";
import React, { useState } from 'react';
import Header from '@/components/Header';

function Page() {
  const [textValue, setTextValue] = useState('');
  const [wordCount, setWordCount] = useState(0);
  const [charCount, setCharCount] = useState(0);
  const [readingTime, setReadingTime] = useState(0);
  const [complexity, setComplexity] = useState('Easy');

  const handleChange = (e) => {
    const inputText = e.target.value;
    setTextValue(inputText);

    // Count characters
    setCharCount(inputText.length);

    // Count words
    const words = inputText.trim().split(/\s+/);
    setWordCount(words.length);

    // Calculate reading time (assuming 200 words per minute)
    const time = Math.ceil(words.length / 200);
    setReadingTime(time);

    // Calculate complexity (basic example)
    if (words.length > 100) {
      setComplexity('Hard');
    } else if (words.length > 50) {
      setComplexity('Medium');
    } else {
      setComplexity('Easy');
    }
  };

  const clearText = () => {
    if (textValue.trim()) {
      setTextValue('');
      setWordCount(0);
      setCharCount(0);
      setReadingTime(0);
      setComplexity('Easy');
    }
  };

  return (
    <>
      <Header />
      <div className="container-fluid bg-light vh-100">
        <div className="container">
          <div className="row">
            <div className="col-8">
              <h1>Text Analyzer</h1>
            </div>
            <div className="col-4 mt-3">
              <span className="btn border">copy</span>{' '}
              <span onClick={clearText} className="btn border">
                clear
              </span>
            </div>
          </div>
          <div className="row">
            <div className="col-12">
              <textarea
                value={textValue}
                onChange={handleChange}
                style={{ width: '100%', height: '15em' }}
                placeholder="Enter your text here"
              ></textarea>
            </div>
          </div>
          <div className="row">
            <div className="col-3">
              <div
                style={{
                  backgroundColor: '#E8F9FF',
                  color: '#9381ff',
                }}
                className="card"
              >
                <p className="p-1">Characters</p>
                <p>{wordCount}</p>
              </div>
            </div>
            <div className="col-3">
              <div
                style={{
                  backgroundColor: '#C2FFC7',
                  color: '#5CB338',
                }}
                className="card"
              >
                <p className="p-1">Words</p>
                <p>{charCount}</p>
              </div>
            </div>
            <div className="col-3">
              <div
                style={{
                  backgroundColor: '#F5EFFF',
                  color: '#8B5DFF',
                }}
                className="card"
              >
                <p className="p-1">Reading Time</p>
                <p>{readingTime} min</p>
              </div>
            </div>
            <div className="col-3">
              <div
                style={{
                  backgroundColor: '#FCFFC1',
                  color: '#F26B0F',
                }}
                className="card"
              >
                <p className="p-1">Complexity</p>
                <p>{complexity}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Page;