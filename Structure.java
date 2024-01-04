import javax.management.RuntimeErrorException;

public class Structure {
    
    protected String type;
    protected String geo;
    protected float strike;
    protected float dip;
    protected float thickness;
    protected float X;
    protected float Y;
    protected float Z;

    Structure(String type, String geo, float strike, float dip, float thickness, float X, float Y, float Z){
        this.setType(type);
        this.setGeo(geo);
        this.setStrike(strike);
        this.setDip(dip);
        this.setThick(thickness);
        this.setX(X);
        this.setY(Y);
        this.setZ(Z);
    }

    Structure(String type, String geo, float strike, float dip, float X, float Y){
        this.setType(type);
        this.setGeo(geo);
        this.setStrike(strike);
        this.setDip(dip);
        this.setX(X);
        this.setY(Y);
        this.setZ(Z);
    }
    
    //setters

    public String setType(String strucType){
        return strucType;
    }

    public String setGeo(String geologist){
        return geologist;
    }

    public float setStrike(float strike){
        if ((strike >= 0) && (strike <= 360)){
            return strike;
        }else{
            return (-42069);
        }
    }

    public float setDip(float dip){
        if ((dip >= -90) && (dip <= 90)){
            return dip;
        }else{
            return (-42069);
        }
    }

    public float setThick(float thick){
        return thick;
    }

    public float setX(float X){
        return X;
    }

    public float setY(float Y){
        return Y;
    }

    public float setZ(float Z){
        return Z;
    }

    //getters

    public String getType(){
        return this.type;
    }

    public String getGeo(){
        return this.geo;
    }

    public float[] getStrikeDip(){
        float[] strikeDips = new float[2];
        strikeDips[0] = this.strike;
        strikeDips[1] = this.dip;
        return strikeDips;
    }

    public float getThick(){
        return this.thickness;
    }

    public float[] getCoord(){
        float[] xyz = new float[3];
        xyz[0] = this.X;
        xyz[1] = this.Y;
        xyz[2] = this.Z;
        return xyz;
    }
    
}
