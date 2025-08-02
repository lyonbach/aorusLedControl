use std::{thread, time::Duration};
use hidapi::HidApi;

const IT8297_RGB_CONTROLLER_VENDOR_ID: u16 = 0x048d;
const IT8297_RGB_CONTROLLER_PRODUCT_ID: u16 = 0x8297;

const FEATURE_REPORT_COLOR: [u8; 23] = [
    0xcc, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x5a, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
];
const FEATURE_REPORT_COMMIT: [u8; 23] = [
    0xcc, 0x28, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
];

// Aorus I X570 PRO WIFI INFO
// idVendor           0x048d Integrated Technology Express, Inc.
// idProduct          0x8297 IT8297 RGB LED Controller


struct It8297RgbController {
    device: hidapi::HidDevice,
    feature_report_color: [u8; 23],
}

impl It8297RgbController {
    pub fn new(api: &HidApi) -> Result<Self, hidapi::HidError> {
        let device = api.open(
            IT8297_RGB_CONTROLLER_VENDOR_ID,
            IT8297_RGB_CONTROLLER_PRODUCT_ID,
        )?;
        Ok(It8297RgbController {
            device,
            feature_report_color: FEATURE_REPORT_COLOR,
        })
    }

    pub fn set_color(&mut self, color: &[u8; 3]) {
        self.feature_report_color[16] = color[0]; // R
        self.feature_report_color[15] = color[1]; // G
        self.feature_report_color[14] = color[2]; // B
        let _ = self.send_report();
        let _ = self.commit();
    }

    pub fn send_report(&self) {
        match self.device.send_feature_report(&self.feature_report_color) {
            Ok(_) => {
                // Report sent successfully
            }
            Err(e) => {
                eprintln!("Failed to send feature report: {}", e);
            }
        }
    }

    pub fn commit(&self) {
        match self.device.send_feature_report(&FEATURE_REPORT_COMMIT) {
            Ok(_) => {}
            Err(e) => {
                eprintln!("Failed to send feature report: {}", e);
            }
        }
    }

    pub fn set_led_idx(&mut self, idx: u8) {
        let clamped_idx = idx.clamp(0, 4);
        self.feature_report_color[1] = 0x20 + clamped_idx;
        self.feature_report_color[2] = 0x01 << idx;
    }
}

#[allow(while_true)]
fn main() {
    let api = HidApi::new().expect("Failed to create HidApi instance");

    match It8297RgbController::new(&api) {
        
        Ok(mut controller) => {

            while true {
                let mut color: [u8;3] = [255, 20, 0];
                controller.set_led_idx(0);
                controller.set_color(&color);
                controller.set_led_idx(1);
                controller.set_color(&color);
                controller.set_led_idx(2);
                controller.set_color(&color);
                controller.set_led_idx(3);
                controller.set_color(&color);
    
                thread::sleep(Duration::new(2, 0));
                
                color = [0, 0, 0];
                controller.set_led_idx(0);
                controller.set_color(&color);
                controller.set_led_idx(1);
                controller.set_color(&color);
                controller.set_led_idx(2);
                controller.set_color(&color);
                controller.set_led_idx(3);
                controller.set_color(&color);
                
                thread::sleep(Duration::new(2, 0));
            }
        }
        Err(e) => {
            eprintln!("Failed to open the device!, {}", e);
        }
    }
}
