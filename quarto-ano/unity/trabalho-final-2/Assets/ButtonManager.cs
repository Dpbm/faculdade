using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class ButtonManager : MonoBehaviour
{

    public AudioSource audio;

    [SerializeField] private SpriteState spriteState;
    [SerializeField] private Button button;


    void Update(){
        // TODO: CHANGE BACK TO THE DEFAULT SPRITE
    }


    public void playAudio(){
        if(audio.isPlaying) return;
        
        button.spriteState = spriteState;
        audio.Play();
    }

}
