__author__="Gábor Tóth-Molnár"
__version__="1.2.1"

# changelog:
# 1.2.1:
# FileConverters renamed to FileTweaks. LogFilenameGenerator added to this class.
#
# 1.2.0:
# added class: Science with CelsiusToFahrenheit and FahrenheitToCelsius, HeatIndex and HeatIndexSafetyLevel
#
# 1.1.3:
# added option to CsvColumnToArray: skip dummy lines beside header
#
# 1.1.2:
# in FileConverters CsvColumnToArray tries to return float() values
#
# 1.1.1:
# appended class Statistics with Rescale, MeanNormalization
#
# 1.1:
# added class: FileConverters with CsvColumnToArray
# appended class Statistics: with MovingAverage,StandardDeviation, FractionalStandardDeviation, StandardScore
# exception handling in ArithmeticMean
#
# 1.0:
# added class: Statistics with ArithmeticMean,GeometricMean,HarmonicMean,Mode, Median, GeneralizedMean





class Statistics:
    def __init__(self):
        pass

    def ArithmeticMean(dataset):
        "returns the arithmetic mean of the input list"
        sum=0.0
        for i in range(0, len(dataset)):
            try:
                sum+=dataset[i]
            except:
                raise TypeError("Array has a NaN element")
        try:
            return sum/len(dataset)
        except ZeroDivisionError:
            raise ZeroDivisionError("Length of dataset is 0.")

    def GeometricMean(dataset):
        "returns the geometric mean of the input list"
        prod=1.0
        for i in range(0, len(dataset)):
            try:
                prod*=dataset[i]
            except:
                raise TypeError("Dataset has a NaN element")
        try:
            return pow(prod,(1/len(dataset)))
        except ZeroDivisionError:
            raise ZeroDivisionError("Length of dataset is 0.")

    def HarmonicMean(dataset):
        "returns the harmonic mean of the input list"
        denominator=0.0
        for i in range(0,len(dataset)):
            try:
                denominator+=(1.0/dataset[i])
            except ZeroDivisionError:
                raise ZeroDivisionError("Dataset contains a 0.")
        try:
            return len(dataset)/denominator
        except ZeroDivisionError:
            raise ZeroDivisionError("Length of dataset is 0.")

    def Mode(dataset):
        "returns the mode of the input list"
        try:
            return max(dataset, key=dataset.count)
        except ValueError:
            raise ValueError("Length of dataset is 0.")

    def Maximum(dataset):
        "returns the maximum value of the input list"
        try:
            return max(dataset)
        except TypeError:
            raise TypeError("Dataset has a NaN element")
        except ValueError:
            raise ValueError("Length of dataset is 0.")

    def Minimum(dataset):
        "returns the minimum value of the input list"
        try:
            return min(dataset)
        except TypeError:
            raise TypeError("Dataset has a NaN element")
        except ValueError:
            raise ValueError("Length of dataset is 0.")

    def Median(dataset,self):
        "returns the median of the input list"
        try:
            for i in range(0, len(dataset)):
                float(dataset[i])
        except ValueError:
            raise ValueError("Dataset has a NaN element")
        length=len(dataset)
        if length==0:
            raise ValueError("Length of dataset is 0.")
        elif length%2!=0:
            return dataset[int(length/2-0.5)]
        else:
            return self.ArithmeticMean([dataset[int(length/2)], dataset[int(length/2-1)]])

    def GeneralizedMean(dataset, power):
        "returns the generalized mean of the input list. Can be RMS with power of 2"
        sum = 0.0
        for i in range(0, len(dataset)):
            try:
                sum += pow(dataset[i], power)
            except:
                raise TypeError("Array has a NaN element")
        try:
            return pow(sum/len(dataset),1/power)
        except ZeroDivisionError:
            raise ZeroDivisionError("Either power or Length of dataset is 0.")

    def MidRange(dataset, self):
        "returns the value in the middle of the range of the input list"
        return (self.Minimum(dataset)+self.Maximum(dataset))/2.0

    def MovingAverage(dataset, window,self):
        "returns the moving average of the input list according to the window"
        beginhere=0
        endhere=window
        output=[]
        for i in range(0, len(dataset)-window):
            output.append(self.ArithmeticMean(dataset[beginhere:endhere]))
            beginhere+=1
            endhere+=1
        return output

    def StandardDeviation(dataset,denominator, self):
        "returns the standard deviation of the dataset according to the denominator string: N or N-1"
        sum=0.0
        avg=self.ArithmeticMean(dataset)
        for i in range(0, len(dataset)):
            sum+=pow((dataset[i]-avg),2)
        if denominator=="N":
            return pow((sum/len(dataset)),0.5)
        elif denominator=="N-1":
            return pow((sum / (len(dataset)-1)), 0.5)
        else:
            raise NameError("Denominator argument must be 'N' or 'N-1'")

    def FractionalStandardDeviation(dataset,denominator, self):
        "returns the fractional standard deviation of the dataset according to the denominator string: N or N-1"
        return self.StandardDeviation(dataset, denominator,self)/self.ArithmeticMean(dataset)*100

    def StandardScore(dataset,denominator, self):
        "return the standard score (Z-score, Z-value) of the input dataset"
        output=[]
        std=self.StandardDeviation(dataset, denominator,self)
        avg=self.ArithmeticMean(dataset)
        for i in range(0, len(dataset)):
            output.append((dataset[i]-avg)/std)
        return output

    def Rescale(dataset, self):
        "returns the rescaled values to [0,1] range of the dataset"
        output=[]
        min=self.Minimum(dataset)
        max=self.Maximum(dataset)
        for i in range(0, len(dataset)):
            try:
                output.append((dataset[i]-min)/(max-min))
            except ZeroDivisionError:
                raise ZeroDivisionError("Dataset has no range")
        return output

    def MeanNormalization(dataset, self):
        "returns the MeanNormalized values of the dataset"
        min = self.Minimum(dataset)
        max = self.Maximum(dataset)
        avg = self.ArithmeticMean(dataset)
        output=[]
        for i in range(0, len(dataset)):
            try:
                output.append((dataset[i]-avg)/(max-min))
            except ZeroDivisionError:
                raise ZeroDivisionError("Dataset has no range")
        return output




class FileTweaks:
    def __init__(self):
        pass
    def CsvColumnToArray(CsvFile,IsHeader, HumanMode, columns,delimiter,DummyLinesBesideHeader=0):
        "CsvFile: the inputfile-----IsHEader: if the first line should be omitted-----Humanmode: index of first column is 1st instead of 0th.------columns: list containing column indexes according to Humanmode------delimiter: delimiter string of the csv file"
        inputFile=open(CsvFile, "r",encoding="UTF-8")
        inputFile.seek(0)
        output=[]
        for i in range(0, len(columns)):
            output.append([])
        for i in range(0,DummyLinesBesideHeader):
            inputFile.readline()
        if IsHeader:
            inputFile.readline()
        for line in inputFile:
            snippedtobeList = [x.strip() for x in line.split(delimiter)]
            for i in range(0, len(columns)):
                try:
                    if HumanMode:
                        output[i].append(float(snippedtobeList[columns[i]-1]))
                    else:
                        output[i].append(float(snippedtobeList[columns[i]]))
                except:
                    raise TypeError("Array has a NaN element")
        return output

    def LogFilenameGenerator(folder,CommonName):
        "generates a running index in the filename"
        import os.path
        for i in range(1, 1000):
            FileSerial = str(i)
            LogFileName = str(CommonName)+'_' + FileSerial.zfill(3) + '.csv'
            LogFile = os.path.join(folder, LogFileName)
            IsFile = os.path.isfile(LogFile)
            if not IsFile:
                return LogFile

class Science:
    def __init__(self):
        pass
    def CelsiusToFahrenheit(degC):
        return degC*1.8+32

    def FahreinheitToCelsius(degF):
        return (degF-32.0)/1.8

    def HeatIndex(degF,RH, self, SunExposure=False,degC=True):
        "returns the heat index in Celsius or Fahrenheit value"
        c1=-42.379
        c2=2.04901523
        c3=10.14333127
        c4=-0.22475541
        c5=-6.83783*pow(10,-3)
        c6=-5.481717*pow(10,-2)
        c7=1.22874*pow(10,-3)
        c8=8.5282*pow(10,-4)
        c9=-1.99*pow(10,-6)
        if degC:
            HI=self.FahreinheitToCelsius(c1+c2*degF+c3*RH+c4*degF*RH+c5*pow(degF,2)+c6*pow(RH,2)+c7*pow(degF,2)*RH+c8*degF*pow(RH,2)+c9*pow(degF,2)*pow(RH,2))
            if SunExposure:
                return HI+8.0
            else:
                return HI
        else:
            HI=c1+c2*degF+c3*RH+c4*degF*RH+c5*pow(degF,2)+c6*pow(RH,2)+c7*pow(degF,2)*RH+c8*degF*pow(RH,2)+c9*pow(degF,2)*pow(RH,2)
            if SunExposure:
                return HI+14.0
            else:
                return HI

    def HeatIndexSafetyLevel(HI, degC=True):
        "returns the safety level and risks according to the heat index."
        levels=["Caution",
                "Extreme Caution",
                "Danger",
                "Extreme Danger"]

        warnings=["Fatigue is possible with prolonged exposure and activity. Continuing activity could result in heat cramps.",
                  "Heat cramps and heat exhaustion are possible. Continuing activity could result in heat stroke.",
                  "Heat cramps and heat exhaustion are likely; heat stroke is probable with continued activity.",
                  "Heat stroke is imminent."]
        if degC:
            if HI>27.0 and HI<=32.0:
                return levels[0],warnings[0]
            elif HI>32.0 and HI<=39.0:
                return levels[1], warnings[1]
            elif HI>39.0 and HI<=51.0:
                return levels[2], warnings[2]
            elif HI>51.0:
                return levels[3], warnings[3]
        else:
            if HI>80.0 and HI<=90.0:
                return levels[0],warnings[0]
            elif HI>90.0 and HI<=103.0:
                return levels[1], warnings[1]
            elif HI>103.0 and HI<=123.0:
                return levels[2], warnings[2]
            elif HI>123.0:
                return levels[3], warnings[3]
