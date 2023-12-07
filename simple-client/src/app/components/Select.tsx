import React, { useState } from 'react';

interface SelectProps {
    options: string[];
    onChange: (value: string) => void;
    placeholder?: string; // Add a placeholder prop
    title?: string; // Add a title prop
}

const Select: React.FC<SelectProps> = ({ options, onChange, placeholder, title }) => {
    const [selectedOption, setSelectedOption] = useState<string>('');

    const handleSelectChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
        const value = event.target.value;
        setSelectedOption(value);
        onChange(value);
    };

    return (
        <div>
            {title && <h3>{title}</h3>} {/* Render the title if provided */}
            <select
                value={selectedOption}
                onChange={handleSelectChange}
                className="p-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
                {placeholder && (
                    <option value="" disabled selected>
                        {placeholder}
                    </option>
                )} {/* Render the placeholder if provided */}
                {options.map((option) => (
                    <option key={option} value={option}>
                        {option}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default Select;
