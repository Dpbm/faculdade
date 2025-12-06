using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;

public class Camera_Control : MonoBehaviour
{

    private Vector2 mouseLook;
    private Vector2 smoothV;

    public float sensitivity = 5f;
    public float smoothing = 2f;

    private GameObject personagem;

    void Start()
    {
        personagem = this.transform.parent.gameObject; 
    }

    // Update is called once per frame
    void Update()
    {
       Vector2 md = new Vector2(Input.GetAxisRaw("Mouse X"), Input.GetAxisRaw("Mouse Y"));
       md = Vector2.Scale(md, new Vector2(sensitivity*smoothing, sensitivity*smoothing));
       smoothV.x = Mathf.Lerp(smoothV.x, md.x, 1f/smoothing);
       smoothV.y = Mathf.Lerp(smoothV.y, md.y, 1f/smoothing);
       mouseLook = mouseLook + smoothV;


       transform.localRotation = Quaternion.AngleAxis(-mouseLook.y, Vector3.right);
       personagem.transform.localRotation = Quaternion.AngleAxis(mouseLook.x,personagem.transform.up);
    }
}
