package com.example.mobilecomputing;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.IOException;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class UploadActivity extends AppCompatActivity {

    // Video Source - https://www.youtube.com/watch?v=tCIL_CxxdrY
    byte[] imageAsArray;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.uploadactivity);

        Bundle info = getIntent().getExtras();
        imageAsArray = info.getByteArray("picture");
        Bitmap pic = BitmapFactory.decodeByteArray(imageAsArray, 0, imageAsArray.length);
        ImageView capturedImage = (ImageView) findViewById(R.id.imageView);
        capturedImage.setImageBitmap(pic);

        Button upload=(Button) findViewById(R.id.buttonupload);
        upload.setOnClickListener(new  View.OnClickListener(){
            public void onClick(View view){
                ImageToServer();
            }
        });
    }
    // Source - https://square.github.io/okhttp/
    private void ImageToServer() {
        String url = "http://10.0.2.2:"+5000+"/";
        MultipartBody.Builder obj = new MultipartBody.Builder().setType(MultipartBody.FORM);
        obj.addFormDataPart("image", "image"+ ".jpg", RequestBody.create(MediaType.parse("image/*jpg"), imageAsArray));
        RequestBody requestObject = obj.build();
        OkHttpClient httpHelper = new OkHttpClient();
        Request flaskRequest = new Request.Builder().post(requestObject).url(url).build();

        httpHelper.newCall(flaskRequest).enqueue(new Callback() {
            public void onResponse(Call call, final Response response) throws IOException {
                Intent refreshPage = new Intent(UploadActivity.this, MainActivity.class);
                startActivity(refreshPage);
            }

            public void onFailure(final Call call, final IOException e) {
            }
        });
    }
}