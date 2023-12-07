import React, { useState } from 'react';

interface DateSelectProps {
    onDateChange: (date: Date) => void;
}

const DateSelect: React.FC<DateSelectProps> = ({ onDateChange }) => {
    const [selectedDate, setSelectedDate] = useState<Date | null>(null);

    const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const date = new Date(event.target.value);
        setSelectedDate(date);
        onDateChange(date);
    };

    return (
        <div className="flex items-center justify-center">
            <input
                type="date"
                id="date"
                className="px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                onChange={handleDateChange}
            />
        </div>
    );
};

export default DateSelect;
