import React, { useEffect, useRef, useState } from 'react';
import QrScanner from 'qr-scanner';
import QrFrame from '../../assets/qr-frame.svg';
import "./QrStyle.css";

const QrScan = () => {
  const scanner = useRef();
  const videoEl = useRef(null);
  const qrBoxEl = useRef(null);
  const [qrOn, setQrOn] = useState(true);
  const [scannedResult, setScannedResult] = useState("");

  const onScanSuccess  = async (result) => {
    if (result) {
      console.log('Scanned Qr Code: ', result)
      setScannedResult(result?.data);
    }
  };
  const onScanFail = (err) => {
    console.error('QR code scan error:', err)
  }

  useEffect(() => {
    if (videoEl?.current && !scanner.current){
      scanner.current = new QrScanner(videoEl?.current, onScanSuccess , {
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
          if (err) setQrOn(false)
        });
    }
    return () => {
      if (!videoEl?.current) {
        scanner?.current.stop()
      }
    }
  }, []);
  useEffect(() => {
    if (!qrOn)
      alert(
        "Camera is blocked or not accessible. Please allow camera in your browser permissions and Reload."
      );
  }, [qrOn]);
  return (
    <div className='qr-reader'>
        <video ref={videoEl}></video>
        <div ref={qrBoxEl} className='qr-box'>
          <img
            src={QrFrame}
            alt='Qr Frame'
            width={256}
            height={256}
            className='qr-frame'
          />
        </div>
        {scannedResult && (
        <p
          style={{
            position: "absolute",
            top: 0,
            left: 0,
            zIndex: 99999,
            color: "white",
          }}
        >
          Scanned Result: {scannedResult}
        </p>
      )}
    </div>
  );
};

export default QrScan;
