import React, { useState, useEffect } from 'react';

/**
 * Alert component.
 * 
 * This component displays an alert message with optional duration.
 * 
 * @param message - The message to be displayed in the alert.
 * @param duration - The duration for which the alert should be visible (in milliseconds).
 * @returnsThe JSX element representing the alert component.
 */
const Alert = ({ message, duration = 3000 }) => {
    const [visible, setVisible] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setVisible(false);
        }, duration);

        return () => clearTimeout(timer);
    }, [duration]);

    if (!visible) return null;

    // Define the animation keyframes directly in the component
    const fadeInOut = {
        '0%': { opacity: 0 },
        '50%': { opacity: 1 },
        '100%': { opacity: 0 },
    };

    // Apply the animation to the alert
    const alertStyle = {
        animation: `fadeInOut 3s forwards`,
        animationFillMode: 'forwards',
    };

    return (
        <div className="fixed top-4 left-1/2 transform -translate-x-1/2 bg-green-500 text-white px-5 py-2 rounded-md z-50" style={alertStyle}>
            {message}
        </div>
    );
};

export default Alert;