import { useState, useEffect } from "react";

type NiftiViewerProps = {
  imgBase64Code: string;
  containerId: number;
};

function NiftiViewer({ imgBase64Code, containerId }: NiftiViewerProps) {
  useEffect(() => {
    if (typeof papaya !== "undefined") {
      //manually stat papayajs
      papaya.Container.startPapaya();
    }

    if (imgBase64Code) {
      let finalVal = `data:image/nifti;base64,${imgBase64Code}`;
      let params = [];
      params["showControlBar"] = true;
      params["images"] = [finalVal];

      //look for the index of container associated to the given ID
      // this is a workaround to have a reference of the container
      // to work with, since papaya js overwrites the ids
      const index = papayaContainers.findIndex(
        (x) => x.containerHtml.context.getAttribute("meta-id") == containerId,
      );

      papaya.Container.resetViewer(index, params);

      // for some reason using addViewer didnt work at all,
      // when adding dinamically containers
      // papaya.Container.addViewer("4", params);
    }
  }, [imgBase64Code]);

  return (
    <>
      <div className="row">
        <div className="col-8">
          <div
            className="papaya"
            data-params="params"
            meta-id={containerId}
            id=""
          ></div>
        </div>
      </div>
    </>
  );
}

export default NiftiViewer;
