import React, { useEffect, useState } from "react";

const GenerateQRcode = () => {
    const url = 'https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Example'
    const [qrCode, setQRCode] = useState("");
    const fetchImage = async () => {
        const res = await fetch(url);
        const blob = await res.blob();
        const qrCodeURL = URL.createObjectURL(blob);
        setQRCode(qrCodeURL);
      };
    
  return (
    <div className="mx-auto my-5 relative bg-white width min-h-16 pb-5 w-96">
      <svg
          className="h-12 absolute top-2 right-4"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 448 512"
          onClick={fetchImage}
        >
          <path
            stroke-width="2"
            d="M0 80C0 53.5 21.5 32 48 32h96c26.5 0 48 21.5 48 48v96c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V80zM64 96v64h64V96H64zM0 336c0-26.5 21.5-48 48-48h96c26.5 0 48 21.5 48 48v96c0 26.5-21.5 48-48 48H48c-26.5 0-48-21.5-48-48V336zm64 16v64h64V352H64zM304 32h96c26.5 0 48 21.5 48 48v96c0 26.5-21.5 48-48 48H304c-26.5 0-48-21.5-48-48V80c0-26.5 21.5-48 48-48zm80 64H320v64h64V96zM256 304c0-8.8 7.2-16 16-16h64c8.8 0 16 7.2 16 16s7.2 16 16 16h32c8.8 0 16-7.2 16-16s7.2-16 16-16s16 7.2 16 16v96c0 8.8-7.2 16-16 16H368c-8.8 0-16-7.2-16-16s-7.2-16-16-16s-16 7.2-16 16v64c0 8.8-7.2 16-16 16H272c-8.8 0-16-7.2-16-16V304zM368 480a16 16 0 1 1 0-32 16 16 0 1 1 0 32zm64 0a16 16 0 1 1 0-32 16 16 0 1 1 0 32z"
          />
        </svg>
        <h3 className="text-2xl font-medium text-center pt-4">Generate QRcode</h3>
        {qrCode && <img className="max-h-40 mt-2 mx-auto" src={qrCode} alt='QrCode' />}
      </div>
  )
}

export default GenerateQRcode
