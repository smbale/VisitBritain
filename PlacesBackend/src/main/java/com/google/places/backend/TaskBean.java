package com.google.places.backend;

/** The object model for the data we are sending through endpoints */
public class TaskBean {

    private String myData;
    private long id;

    public String getData() {
        return myData;
    }

    public void setData(String data) {
        myData = data;
    }

    


    public String getId() {
        return myData;
    }

    public void setId(long id) {
        this.id = id;
    }
}