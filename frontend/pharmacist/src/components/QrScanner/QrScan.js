import React, { useEffect, useRef, useState } from "react";
import QrScanner from "qr-scanner";
import QrFrame from "../../assets/qr-frame.svg";

/**
 * QrScan Component
 * @param setCallSearch - Function to set the search value based on the scanned QR code.
 * @param setActiveQrScanner - Function to set the active state of the QR scanner.
 * @returns QR scanning component.
 */
const QrScan = ({ setCallSearch, setActiveQrScanner }) => {
  const scanner = useRef();
  const videoEl = useRef(null);
  const qrBoxEl = useRef(null);
  const [qrOn, setQrOn] = useState(true);
  // const [scannedResult, setScannedResult] = useState("");

   /**
   * Callback function invoked when QR code is scanned successfully.
   * @param result - Scanned QR code result.
   */
  const onScanSuccess = async (result) => {
    if (result) {
      console.log("Scanned Qr Code: ", result);
      // setScannedResult(result?.data);
      setCallSearch(result?.data);
      handleCloseButtonClick();
    }
  };

  /**
   * Callback function invoked when QR code scanning fails.
   * @param err - Error object.
   */
  const onScanFail = (err) => {
    console.error("QR code scan error:", err);
  };

  /**
   * Handler function to close the QR scanner.
   */
  const handleCloseButtonClick = () => {
    scanner?.current.stop();
    setQrOn(false);
    setActiveQrScanner(false);
  };

  useEffect(() => {
    if (videoEl?.current && !scanner.current) {
      scanner.current = new QrScanner(videoEl?.current, onScanSuccess, {
        onDecodeError: onScanFail,
        preferredCamera: "environment",
        highlightScanRegion: true,
        highlightCodeOutline: true,
        overlay: qrBoxEl?.current || undefined,
      });

      scanner?.current
        ?.start()
        .then(() => setQrOn(true))
        .catch((err) => {
          if (err) setQrOn(false);
        });
    }
    return () => {
      if (!videoEl?.current) {
        scanner?.current.stop();
      }
    };
  }, []);
  useEffect(() => {
    if (!qrOn)
      alert(
        "Camera is blocked or not accessible. Please allow camera in your browser permissions and Reload."
      );
  }, [qrOn]);
  return (
    <div className="w-full lg:w-[50vw] mt-10 lg:mt-20 mx-auto flex flex-col justify-center items-center">
      <video ref={videoEl} className="w-full h-full object-cover" />
      <div ref={qrBoxEl} className="w-full left-0">
        <img
          src={QrFrame}
          alt="Qr Frame"
          width={256}
          height={256}
          className="absolute fill-none left-[50%] top-[50%] translate-x-[-50%] translate-y-[-50%]"
        />
      </div>

      {qrOn && (
        <button
          className="bg-red text-white py-2 px-4 rounded-md shadow-md"
          onClick={handleCloseButtonClick}
        >
          Close
        </button>
      )}
      {/* {scannedResult && console.log(scannedResult)} */}
      {/* {scannedResult && <Searchbox scannedId={scannedResult} />} */}

    </div>
  );
};

export default QrScan;
