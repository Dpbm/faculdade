using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Personagem : MonoBehaviour
{

    public float velMov = 10f;

    void Start()
    {
        Cursor.lockState = CursorLockMode.Locked; 
    }

    void Update()
    {
        float translation = Input.GetAxis("Vertical") * velMov;
        float straffe = Input.GetAxis("Horizontal") * velMov;
        translation *= Time.deltaTime;
        straffe *= Time.deltaTime;

        transform.Translate(straffe, 0, translation);

        if(Input.GetKeyDown("escape")){
            Cursor.lockState = CursorLockMode.None; 
        }
    }
}
