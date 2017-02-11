using UnityEngine;
using System.Collections;
using UnityEngine.UI;

public class PlayerControllerrr : MonoBehaviour {

	// all public show up in the inspector
	public float speed;
	public Text countText;
	public Text winText; 
	public AudioClip winSound;

	private Rigidbody rb;
	private int count;
	private GameObject[] getCount;
	private int numPickUp;
	private AudioSource source;

	//Update is called before rendering a frame--for most game code
	//void Update()
	//{

	//}
	//FixedUpdate is called before performing physics calculations-physics goes here
	//Start is called on the first frame that the script is active, generally first of the game
	void Start()
	{
		rb = GetComponent<Rigidbody> ();
		count = 0;
		SetCountText ();
		winText.text = "";
		getCount = GameObject.FindGameObjectsWithTag ("Pick Up"); 
		numPickUp = getCount.Length;
		source = GetComponent<AudioSource>();

	}
	void FixedUpdate()
	{
		//floats store inputs from the getaxis functions controlled by the keyboard
		float moveHorizontal = Input.GetAxis ("Horizontal");
		float moveVertical = Input.GetAxis ("Vertical");

		Vector3 movement = new Vector3 (moveHorizontal, 0, moveVertical);

		rb.AddForce (movement * speed);
	}
	void OnTriggerEnter (Collider other)
	{

		if (other.gameObject.CompareTag ("Pick Up")) 
		{
			count += 1;
			other.gameObject.SetActive (false); 
			SetCountText ();
		}

	}
	void SetCountText ()
	{		
		countText.text = "Count: " + count.ToString () ;
		if (count >= numPickUp) 
		{
			winText.text = "You Win!" ;
			source.PlayOneShot (winSound);
		}
	}
}

//Deactivate(other.gameObject);
