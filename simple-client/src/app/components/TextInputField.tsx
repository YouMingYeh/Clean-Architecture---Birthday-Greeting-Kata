import React, { ChangeEvent } from 'react';

interface TextInputFieldProps {
    value: string;
    onChange: (value: string) => void;
    placeholder?: string;
}

const TextInputField: React.FC<TextInputFieldProps> = ({ value, onChange, placeholder }) => {
    const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
        onChange(event.target.value);
    };

    return (
        <input
            type="text"
            value={value}
            onChange={handleInputChange}
            placeholder={placeholder}
            className="border border-gray-300 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
    );
};

export default TextInputField;
