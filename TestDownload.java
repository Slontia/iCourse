package Desktop;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class TestDownload {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	  System.setProperty("webdriver.gecko.driver", "C:\\Users\\15061188\\Downloads\\geckodriver-v0.19.0-win32\\geckodriver.exe");
    driver = new FirefoxDriver();
    baseUrl = "http://10.2.28.124:8000/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testDownload() throws Exception {
    driver.get("http://10.2.28.124:8000/course");
    driver.findElement(By.xpath("//div[@id='header']/div/div/div[2]/ul/li[2]")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/div/div[2]/div/span[2]")).click();
    driver.findElement(By.xpath("//div[@id='course']/div[2]/div/div[2]/div[2]/div[8]/div")).click();
    driver.findElement(By.xpath("(//button[@type='button'])[11]")).click();
    driver.findElement(By.xpath("(//button[@type='button'])[11]")).click();
    driver.findElement(By.xpath("//div[@id='resource']/div[2]/div[5]/div[2]/div/div/div[2]")).click();
    driver.findElement(By.cssSelector("div.el-row > button.el-button.el-button--primary")).click();
    // ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp |  | 30000]]
    driver.findElement(By.cssSelector("#resource > div.el-dialog__wrapper > div.el-dialog.el-dialog--tiny > div.el-dialog__footer > span.dialog-footer > button.el-button.el-button--default")).click();
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
