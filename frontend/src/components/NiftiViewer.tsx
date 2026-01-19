import { useState, useEffect } from "react";

type NiftiViewerProps = {
  imgBase64Code: string;
};

function NiftiViewer({ imgBase64Code }: NiftiViewerProps) {
  useEffect(() => {
    //manually stat papayajs
    if (typeof papaya !== "undefined" && imgBase64Code) {
      papaya.Container.startPapaya();

      let finalVal = `data:image/nifti;base64,${imgBase64Code}`;
      let params = [];
      params["showControlBar"] = true;
      params["images"] = [finalVal];
      params["containerID"] = "1234";
      papaya.Container.resetViewer(0, params);
      console.log(papayaContainers)
    }
  }, [imgBase64Code]);

  return (
    <>
      <div className="row">
        <div className="col-8">
          <div className="papaya" data-params="params" id="ii"></div>
        </div>
      </div>
    </>
  );
}

export default NiftiViewer;
