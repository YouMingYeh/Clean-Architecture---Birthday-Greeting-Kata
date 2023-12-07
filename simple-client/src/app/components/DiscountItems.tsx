import React, { useState, ChangeEvent } from 'react';

interface DiscountItemsInputProps {
    initialDiscount: number;
    initialItems: string[];
    onDiscountChange: (discount: number) => void;
    onItemsChange: (items: string[]) => void;
}

const DiscountItemsInput: React.FC<DiscountItemsInputProps> = ({
    initialDiscount,
    initialItems,
    onDiscountChange,
    onItemsChange,
}) => {
    const [discount, setDiscount] = useState<number>(initialDiscount);
    const [items, setItems] = useState<string>(initialItems.join(', '));

    const handleDiscountChange = (event: ChangeEvent<HTMLInputElement>) => {
        setDiscount(Number(event.target.value));
        onDiscountChange(Number(event.target.value));
    };

    const handleItemsChange = (event: ChangeEvent<HTMLInputElement>) => {
        setItems(event.target.value);
        onItemsChange(event.target.value.split(',').map((item) => item.trim()));
    };

    return (
        <div className="flex flex-col space-y-4">
            <label>
                <p>Discount: </p>
                <input
                    type="number"
                    value={discount}
                    onChange={handleDiscountChange}
                    className="ml-2 border-2 border-gray-300 rounded-md p-1"
                />
            </label>
            <label>
                <p>Items: </p>
                <input
                    type="text"
                    value={items}
                    onChange={handleItemsChange}
                    className="ml-2 border-2 border-gray-300 rounded-md p-1"
                    placeholder="item1, item2, item3"
                />
            </label>
        </div>
    );
};

export default DiscountItemsInput;