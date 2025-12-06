using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyClass : MonoBehaviour
{
    // Start is called before the first frame update

    public string nome;
    public float velTranslacao;

    // public float velRotacao;
    void Start()
    {
        Debug.Log("UHUUUUUUUU");
    }

    // Update is called once per frame
    void Update()
    {

        Debug.Log("Tome " + this.nome);

        float time = Time.deltaTime;
        float vel = time * velTranslacao;

        if (Input.GetKey("w"))
        {
            transform.Translate(0, 0, vel);
        }

        if (Input.GetKey("s"))
        {
            transform.Translate(0, 0, -vel);
        }

        if (Input.GetKey("a"))
        {
            transform.Translate(-vel, 0, 0);
        }

        if (Input.GetKey("d"))
        {
            transform.Translate(vel, 0, 0);
        }

        if (Input.GetKey(KeyCode.Space))
        {

            transform.Translate(0, vel, 0);
        }

        if (Input.GetKey(KeyCode.LeftShift))
        {

            transform.Translate(0, -vel, 0);
        }


        // Vector3 mouse = time*Input.mousePosition;

        // transform.Rotate(mouse.x, mouse.y, mouse.z);

        // if (Input.GetKey("d"))
        // {
        //     transform.Rotate(0, velRotacao, 0);
        // }


    }
}
